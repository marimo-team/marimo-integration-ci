#!/usr/bin/env python3
"""Visual snapshot tests for `marimo export pdf`.

This script exports a small, deterministic marimo notebook to PDF in both:
- LaTeX/Pandoc mode (`--no-webpdf`)
- WebPDF (Chromium) mode (`--webpdf`)

It rasterizes page 1 at a fixed DPI and compares against committed baseline
PNGs.

Why PNG snapshots (not raw PDF bytes)?
- PDF bytes are high-churn (metadata/toolchain changes).
- Visual diffs are easier to review and much smaller in surface area.

LaTeX mode includes the current date in the rendered output by default; we mask
that date region so snapshots are stable across days.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageOps


REPO_ROOT = Path(__file__).resolve().parents[1]
FIXTURE_NOTEBOOK = REPO_ROOT / "notebooks" / "pdf_snapshot_smoke.py"

SNAPSHOT_NAME = "pdf_snapshot_smoke"

PAGE = 1
DPI = 144


def _baseline_page_1(mode: str) -> Path:
    """Return the baseline PNG path for the given export mode."""
    return REPO_ROOT / "snapshots" / "pdf" / SNAPSHOT_NAME / mode / "page-1.png"


def _artifacts_dir(mode: str) -> Path:
    """Return the artifacts directory path for the given export mode."""
    return REPO_ROOT / "snapshot_artifacts" / "pdf" / SNAPSHOT_NAME / mode


def _run(cmd: list[str], *, timeout_s: int) -> subprocess.CompletedProcess[str]:
    """Run a command and capture stdout/stderr."""
    return subprocess.run(
        cmd,
        cwd=str(REPO_ROOT),
        text=True,
        capture_output=True,
        timeout=timeout_s,
        check=False,
    )


def _find_marimo_cmd() -> list[str]:
    """Return a `marimo` command (prefer PATH, else `python -m marimo`)."""
    marimo = shutil.which("marimo")
    if marimo is not None:
        return [marimo]
    return [sys.executable, "-m", "marimo"]


def _export_pdf(out_pdf: Path, *, webpdf: bool) -> None:
    """Export the fixture notebook to a PDF using marimo's CLI."""
    if not FIXTURE_NOTEBOOK.exists():
        raise FileNotFoundError(f"Fixture notebook not found: {FIXTURE_NOTEBOOK}")

    cmd = [
        *_find_marimo_cmd(),
        "--yes",
        "export",
        "pdf",
        str(FIXTURE_NOTEBOOK),
        "--output",
        str(out_pdf),
        "--include-outputs",
        "--webpdf" if webpdf else "--no-webpdf",
        "--no-sandbox",
    ]

    result = _run(cmd, timeout_s=180)
    if result.returncode == 0:
        return

    combined = f"{result.stdout}\n{result.stderr}"
    if "No such command 'pdf'" in combined:
        raise RuntimeError(
            "`marimo export pdf` not available.\n\n"
            "This repo expects marimo>=0.19.7. Try:\n"
            "  uv sync --extra pdf\n"
        )

    msg = (
        "PDF export failed.\n\n"
        f"Command:\n  {' '.join(cmd)}\n\n"
        f"stdout:\n{result.stdout}\n\n"
        f"stderr:\n{result.stderr}\n"
    )
    raise RuntimeError(msg)


def _rasterize_page(pdf_path: Path, out_png: Path) -> None:
    """Rasterize a single PDF page to PNG using `pdftoppm`."""
    pdftoppm = shutil.which("pdftoppm")
    if pdftoppm is None:
        raise RuntimeError(
            "pdftoppm not found.\n\n"
            "Tip (Ubuntu/Debian): sudo apt-get install poppler-utils\n"
        )

    out_png.parent.mkdir(parents=True, exist_ok=True)

    # `pdftoppm` writes `<prefix>-1.png`; use a stable prefix then rename.
    prefix = out_png.with_suffix("")  # remove .png suffix
    cmd = [
        pdftoppm,
        "-png",
        "-r",
        str(DPI),
        "-f",
        str(PAGE),
        "-l",
        str(PAGE),
        str(pdf_path),
        str(prefix),
    ]

    result = _run(cmd, timeout_s=60)
    if result.returncode != 0:
        msg = (
            "Rasterization failed.\n\n"
            f"Command:\n  {' '.join(cmd)}\n\n"
            f"stdout:\n{result.stdout}\n\n"
            f"stderr:\n{result.stderr}\n"
        )
        raise RuntimeError(msg)

    produced = prefix.with_name(f"{prefix.name}-1.png")
    if not produced.exists():
        raise FileNotFoundError(f"Expected rasterized image not found: {produced}")

    produced.replace(out_png)


def _latex_date_mask_boxes(pdf_path: Path) -> list[tuple[int, int, int, int]]:
    """Return pixel-space boxes to mask LaTeX's dynamic date text."""
    pdftotext = shutil.which("pdftotext")
    if pdftotext is None:
        raise RuntimeError(
            "pdftotext not found.\n\n"
            "Tip (Ubuntu/Debian): sudo apt-get install poppler-utils\n"
        )

    cmd = [
        pdftotext,
        "-bbox",
        "-f",
        str(PAGE),
        "-l",
        str(PAGE),
        str(pdf_path),
        "-",
    ]
    result = _run(cmd, timeout_s=60)
    if result.returncode != 0:
        msg = (
            "Extracting PDF text boxes failed.\n\n"
            f"Command:\n  {' '.join(cmd)}\n\n"
            f"stdout:\n{result.stdout}\n\n"
            f"stderr:\n{result.stderr}\n"
        )
        raise RuntimeError(msg)

    word_re = re.compile(
        r'<word xMin="(?P<x0>[^"]+)" yMin="(?P<y0>[^"]+)" '
        r'xMax="(?P<x1>[^"]+)" yMax="(?P<y1>[^"]+)">(?P<text>[^<]+)</word>'
    )

    words: list[tuple[float, float, float, float, str]] = []
    for m in word_re.finditer(result.stdout):
        try:
            x0 = float(m.group("x0"))
            y0 = float(m.group("y0"))
            x1 = float(m.group("x1"))
            y1 = float(m.group("y1"))
        except ValueError:
            continue
        words.append((x0, y0, x1, y1, m.group("text").strip()))

    def _same_line(y_a: float, y_b: float) -> bool:
        return abs(y_a - y_b) <= 0.75

    def _is_month(s: str) -> bool:
        return s.lower() in {
            "january",
            "february",
            "march",
            "april",
            "may",
            "june",
            "july",
            "august",
            "september",
            "october",
            "november",
            "december",
        }

    def _is_day_with_comma(s: str) -> bool:
        return re.fullmatch(r"\d{1,2},", s) is not None

    def _is_year(s: str) -> bool:
        return re.fullmatch(r"\d{4}", s) is not None

    date_box_pt: tuple[float, float, float, float] | None = None
    for i in range(len(words) - 2):
        (x0a, y0a, x1a, y1a, t1) = words[i]
        (x0b, y0b, x1b, y1b, t2) = words[i + 1]
        (x0c, y0c, x1c, y1c, t3) = words[i + 2]

        if not (_same_line(y0a, y0b) and _same_line(y0b, y0c)):
            continue

        month_day_year = _is_month(t1) and _is_day_with_comma(t2) and _is_year(t3)
        day_month_year = t1.isdigit() and _is_month(t2) and _is_year(t3)
        if not (month_day_year or day_month_year):
            continue

        x0 = min(x0a, x0b, x0c)
        y0 = min(y0a, y0b, y0c)
        x1 = max(x1a, x1b, x1c)
        y1 = max(y1a, y1b, y1c)
        date_box_pt = (x0, y0, x1, y1)
        break

    if date_box_pt is None:
        return []

    (x0_pt, y0_pt, x1_pt, y1_pt) = date_box_pt

    # Convert points (1/72") to pixels at the rasterization DPI.
    scale = DPI / 72.0
    pad_px = 6
    x0_px = int(x0_pt * scale) - pad_px
    y0_px = int(y0_pt * scale) - pad_px
    x1_px = int(x1_pt * scale) + pad_px
    y1_px = int(y1_pt * scale) + pad_px
    return [(x0_px, y0_px, x1_px, y1_px)]


def _mask_boxes(img: Image.Image, boxes: list[tuple[int, int, int, int]]) -> None:
    """Fill rectangular regions with white to hide unstable content."""
    if not boxes:
        return

    draw = ImageDraw.Draw(img)
    for x0, y0, x1, y1 in boxes:
        x0 = max(0, x0)
        y0 = max(0, y0)
        x1 = min(img.width, x1)
        y1 = min(img.height, y1)
        draw.rectangle([x0, y0, x1, y1], fill=(255, 255, 255, 255))


def _normalize_image(mode: str, img: Image.Image, *, pdf_path: Path) -> Image.Image:
    """Mask LaTeX's dynamic date so snapshots are stable across days."""
    if mode != "latex":
        return img

    boxes = _latex_date_mask_boxes(pdf_path)
    if not boxes:
        return img

    normalized = img.copy()
    _mask_boxes(normalized, boxes)
    return normalized


def _compare_images(expected: Image.Image, actual: Image.Image, diff_path: Path) -> bool:
    """Return True if images match; write a diff image when they don't."""
    if expected.size != actual.size:
        diff_path.parent.mkdir(parents=True, exist_ok=True)
        ImageOps.autocontrast(expected).save(diff_path.with_name("expected.png"))
        ImageOps.autocontrast(actual).save(diff_path.with_name("actual.png"))
        return False

    diff = ImageChops.difference(expected, actual)
    if diff.getbbox() is None:
        return True

    diff_path.parent.mkdir(parents=True, exist_ok=True)
    ImageOps.autocontrast(diff).save(diff_path)
    return False


def _run_mode(mode: str, *, update: bool) -> int:
    """Run the snapshot test for a single export mode."""
    if mode not in {"latex", "webpdf"}:
        raise ValueError(f"Unknown mode: {mode}")

    baseline_page_1 = _baseline_page_1(mode)
    artifacts_dir = _artifacts_dir(mode)
    webpdf = mode == "webpdf"

    with tempfile.TemporaryDirectory() as td:
        td_path = Path(td)
        out_pdf = td_path / f"{mode}.pdf"
        out_png = td_path / "page-1.png"

        try:
            _export_pdf(out_pdf, webpdf=webpdf)
        except RuntimeError as e:
            msg = str(e)
            if webpdf and ("playwright" in msg.lower() or "chromium" in msg.lower()):
                msg += (
                    "\n\nTip: WebPDF export requires Chromium. Install it with:\n\n"
                    "  uv run python -m playwright install chromium\n"
                )
            raise RuntimeError(msg) from None

        _rasterize_page(out_pdf, out_png)

        rendered = Image.open(out_png).convert("RGBA")
        rendered = _normalize_image(mode, rendered, pdf_path=out_pdf)

        if update:
            baseline_page_1.parent.mkdir(parents=True, exist_ok=True)
            rendered.save(baseline_page_1)
            print(f"✅ Updated baseline ({mode}): {baseline_page_1.relative_to(REPO_ROOT)}")
            return 0

        if not baseline_page_1.exists():
            print(f"❌ Missing baseline ({mode}): {baseline_page_1.relative_to(REPO_ROOT)}")
            print("   Tip: run `uv run scripts/test_pdf_visual_snapshots.py --update`")
            return 2

        expected = Image.open(baseline_page_1).convert("RGBA")
        expected = _normalize_image(mode, expected, pdf_path=out_pdf)

        if artifacts_dir.exists():
            shutil.rmtree(artifacts_dir)
        artifacts_dir.mkdir(parents=True, exist_ok=True)

        actual_saved = artifacts_dir / "actual-page-1.png"
        diff_saved = artifacts_dir / "diff-page-1.png"
        rendered.save(actual_saved)

        ok = _compare_images(expected, rendered, diff_saved)
        if ok:
            shutil.rmtree(artifacts_dir)
            print(f"✅ PDF visual snapshot matched ({mode}).")
            return 0

        print(f"❌ PDF visual snapshot mismatch ({mode}).")
        print(f"   Baseline: {baseline_page_1.relative_to(REPO_ROOT)}")
        print(f"   Actual:   {actual_saved.relative_to(REPO_ROOT)}")
        print(f"   Diff:     {diff_saved.relative_to(REPO_ROOT)}")
        print("   Tip: if this is expected, update with:")
        print("     uv run scripts/test_pdf_visual_snapshots.py --update")
        return 1


def main() -> int:
    """CLI entrypoint."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--update",
        action="store_true",
        help="Update baseline snapshot(s) in-place instead of comparing.",
    )
    parser.add_argument(
        "--mode",
        action="append",
        choices=["latex", "webpdf"],
        help="Which export mode(s) to test. Repeatable. Defaults to both.",
    )
    args = parser.parse_args()

    modes = args.mode or ["latex", "webpdf"]
    exit_code = 0
    for mode in modes:
        exit_code = max(exit_code, _run_mode(mode, update=args.update))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
