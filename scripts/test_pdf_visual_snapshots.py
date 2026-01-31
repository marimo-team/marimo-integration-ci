#!/usr/bin/env python3
"""Visual snapshot test for `marimo export pdf` (LaTeX/Pandoc).

Exports a small, deterministic marimo notebook to PDF, rasterizes page 1, masks
the dynamic LaTeX date, and compares against a committed baseline PNG.
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
BASELINE_DIR = REPO_ROOT / "snapshots" / "pdf" / SNAPSHOT_NAME
BASELINE_PAGE_1 = BASELINE_DIR / "page-1.png"

ARTIFACTS_DIR = REPO_ROOT / "snapshot_artifacts" / "pdf" / SNAPSHOT_NAME

PAGE = 1
DPI = 144


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


def _export_pdf(out_pdf: Path) -> None:
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
        "--no-webpdf",
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
    """Return pixel-space boxes to mask dynamic LaTeX date text on page 1."""
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
        text = m.group("text").strip()
        words.append((x0, y0, x1, y1, text))

    def _same_line(y_a: float, y_b: float) -> bool:
        return abs(y_a - y_b) <= 0.75

    def _is_month(s: str) -> bool:
        months = {
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
        return s.lower() in months

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


def _normalize_image(img: Image.Image, *, pdf_path: Path) -> Image.Image:
    """Mask LaTeX's dynamic date so snapshots are stable across days."""
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


def main() -> int:
    """CLI entrypoint."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--update",
        action="store_true",
        help="Update baseline snapshot(s) in-place instead of comparing.",
    )
    args = parser.parse_args()

    with tempfile.TemporaryDirectory() as td:
        td_path = Path(td)
        out_pdf = td_path / "out.pdf"
        out_png = td_path / "page-1.png"

        _export_pdf(out_pdf)
        _rasterize_page(out_pdf, out_png)

        rendered = Image.open(out_png).convert("RGBA")
        rendered = _normalize_image(rendered, pdf_path=out_pdf)

        if args.update:
            BASELINE_DIR.mkdir(parents=True, exist_ok=True)
            rendered.save(BASELINE_PAGE_1)
            print(f"✅ Updated baseline: {BASELINE_PAGE_1.relative_to(REPO_ROOT)}")
            return 0

        if not BASELINE_PAGE_1.exists():
            print(f"❌ Missing baseline: {BASELINE_PAGE_1.relative_to(REPO_ROOT)}")
            print("   Tip: run `uv run scripts/test_pdf_visual_snapshots.py --update`")
            return 2

        expected = Image.open(BASELINE_PAGE_1).convert("RGBA")
        expected = _normalize_image(expected, pdf_path=out_pdf)

        # Clean artifact dir (Python-side; avoids shell `rm -rf`).
        if ARTIFACTS_DIR.exists():
            shutil.rmtree(ARTIFACTS_DIR)
        ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

        actual_saved = ARTIFACTS_DIR / "actual-page-1.png"
        diff_saved = ARTIFACTS_DIR / "diff-page-1.png"
        rendered.save(actual_saved)

        ok = _compare_images(expected, rendered, diff_saved)
        if ok:
            shutil.rmtree(ARTIFACTS_DIR)
            print("✅ PDF visual snapshot matched.")
            return 0

        print("❌ PDF visual snapshot mismatch.")
        print(f"   Baseline: {BASELINE_PAGE_1.relative_to(REPO_ROOT)}")
        print(f"   Actual:   {actual_saved.relative_to(REPO_ROOT)}")
        print(f"   Diff:     {diff_saved.relative_to(REPO_ROOT)}")
        print("   Tip: if this is expected, update with:")
        print("     uv run scripts/test_pdf_visual_snapshots.py --update")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

