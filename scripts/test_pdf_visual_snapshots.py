#!/usr/bin/env python3
"""Visual snapshot tests for `marimo export pdf`.

Exports deterministic marimo notebooks to PDF (LaTeX and WebPDF), rasterizes
all pages at a fixed DPI, and compares against committed baseline PNGs.

We snapshot PNGs instead of raw PDF bytes because PDF bytes are high-churn
(metadata/toolchain changes) and visual diffs are easier to review.
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

FIXTURES: dict[str, Path] = {
    "pdf_snapshot_smoke": REPO_ROOT / "notebooks" / "pdf_snapshot_smoke.py",
    "kitchen_sink": REPO_ROOT / "notebooks" / "kitchen_sink.py",
}

DPI = 144

POPPLER_TIPS = [
    "Tip (Ubuntu/Debian): sudo apt-get install poppler-utils",
    "Tip (macOS): brew install poppler",
]


def _page_label(page: int, *, width: int) -> str:
    """Format a page number with zero padding for stable filenames."""
    return str(page).zfill(width)


def _baseline_path(fixture: str, mode: str, page_label: str) -> Path:
    """Return the baseline PNG path for a fixture/mode/page."""
    return (
        REPO_ROOT
        / "snapshots"
        / "pdf"
        / fixture
        / mode
        / f"page-{page_label}.png"
    )


def _artifacts_dir(fixture: str, mode: str) -> Path:
    """Return the artifacts directory path for a fixture/mode."""
    return REPO_ROOT / "snapshot_artifacts" / "pdf" / fixture / mode


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


def _pdf_page_count(pdf_path: Path) -> int:
    """Return the number of pages in a PDF using `pdfinfo`."""
    pdfinfo = shutil.which("pdfinfo")
    if pdfinfo is None:
        raise RuntimeError(
            "\n".join(
                [
                    "pdfinfo not found.",
                    "",
                    *POPPLER_TIPS,
                ]
            )
        )

    result = _run([pdfinfo, str(pdf_path)], timeout_s=30)
    if result.returncode != 0:
        raise RuntimeError(
            "\n".join(
                [
                    "Failed to read PDF metadata.",
                    "",
                    "Command:",
                    f"  {pdfinfo} {pdf_path}",
                    "",
                    "stdout:",
                    result.stdout.rstrip(),
                    "",
                    "stderr:",
                    result.stderr.rstrip(),
                ]
            )
        )

    for line in result.stdout.splitlines():
        if line.startswith("Pages:"):
            try:
                return int(line.split(":", 1)[1].strip())
            except ValueError:
                break

    raise RuntimeError("pdfinfo output did not include a Pages field.")


def _export_pdf(notebook: Path, out_pdf: Path, *, webpdf: bool) -> None:
    """Export a notebook to PDF using marimo's CLI."""
    if not notebook.exists():
        raise FileNotFoundError(f"Notebook not found: {notebook}")

    cmd = [
        *_find_marimo_cmd(),
        "--yes",
        "export",
        "pdf",
        str(notebook),
        "--output",
        str(out_pdf),
        "--include-outputs",
        "--webpdf" if webpdf else "--no-webpdf",
        "--no-sandbox",
    ]

    result = _run(cmd, timeout_s=300)
    if result.returncode == 0:
        return

    combined = "\n".join([result.stdout, result.stderr])
    if "No such command 'pdf'" in combined:
        raise RuntimeError(
            "\n".join(
                [
                    "`marimo export pdf` not available.",
                    "",
                    "This repo expects marimo>=0.19.7. Try:",
                    "  uv sync --extra pdf",
                ]
            )
        )

    raise RuntimeError(
        "\n".join(
            [
                "PDF export failed.",
                "",
                "Command:",
                f"  {' '.join(cmd)}",
                "",
                "stdout:",
                result.stdout.rstrip(),
                "",
                "stderr:",
                result.stderr.rstrip(),
            ]
        )
    )


def _rasterize_page(pdf_path: Path, out_png: Path, *, page: int) -> None:
    """Rasterize a PDF page to PNG using `pdftoppm`."""
    pdftoppm = shutil.which("pdftoppm")
    if pdftoppm is None:
        raise RuntimeError(
            "\n".join(
                [
                    "pdftoppm not found.",
                    "",
                    *POPPLER_TIPS,
                ]
            )
        )

    out_png.parent.mkdir(parents=True, exist_ok=True)

    # `pdftoppm` writes `<prefix>-N.png` where N starts at 1 for the first (and
    # only) produced page, regardless of the PDF page number.
    prefix = out_png.with_suffix("")  # remove .png suffix
    cmd = [
        pdftoppm,
        "-png",
        "-r",
        str(DPI),
        "-f",
        str(page),
        "-l",
        str(page),
        str(pdf_path),
        str(prefix),
    ]

    result = _run(cmd, timeout_s=120)
    if result.returncode != 0:
        raise RuntimeError(
            "\n".join(
                [
                    "Rasterization failed.",
                    "",
                    "Command:",
                    f"  {' '.join(cmd)}",
                    "",
                    "stdout:",
                    result.stdout.rstrip(),
                    "",
                    "stderr:",
                    result.stderr.rstrip(),
                ]
            )
        )

    produced_candidates = sorted(prefix.parent.glob(f"{prefix.name}-*.png"))
    if not produced_candidates:
        raise FileNotFoundError(
            f"Expected rasterized image not found for prefix: {prefix}"
        )

    if len(produced_candidates) != 1:
        names = ", ".join(p.name for p in produced_candidates)
        raise RuntimeError(f"Expected 1 rasterized page, found {len(produced_candidates)}: {names}")

    produced_candidates[0].replace(out_png)


def _latex_date_mask_boxes(pdf_path: Path, *, page: int) -> list[tuple[int, int, int, int]]:
    """Return pixel-space boxes for LaTeX's dynamic date on a page."""
    pdftotext = shutil.which("pdftotext")
    if pdftotext is None:
        raise RuntimeError(
            "\n".join(
                [
                    "pdftotext not found.",
                    "",
                    *POPPLER_TIPS,
                ]
            )
        )

    cmd = [
        pdftotext,
        "-bbox",
        "-f",
        str(page),
        "-l",
        str(page),
        str(pdf_path),
        "-",
    ]
    result = _run(cmd, timeout_s=60)
    if result.returncode != 0:
        raise RuntimeError(
            "\n".join(
                [
                    "Extracting PDF text boxes failed.",
                    "",
                    "Command:",
                    f"  {' '.join(cmd)}",
                    "",
                    "stdout:",
                    result.stdout.rstrip(),
                    "",
                    "stderr:",
                    result.stderr.rstrip(),
                ]
            )
        )

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


def _normalize_image(mode: str, img: Image.Image, *, pdf_path: Path, page: int) -> Image.Image:
    """Mask LaTeX's dynamic date so snapshots are stable across days."""
    if mode != "latex" or page != 1:
        return img

    boxes = _latex_date_mask_boxes(pdf_path, page=page)
    if not boxes:
        return img

    normalized = img.copy()
    _mask_boxes(normalized, boxes)
    return normalized


def _compare_images(
    expected: Image.Image, actual: Image.Image, diff_path: Path, *, page_label: str
) -> bool:
    """Return True if images match; write a diff image when they don't."""
    if expected.size != actual.size:
        diff_path.parent.mkdir(parents=True, exist_ok=True)
        ImageOps.autocontrast(expected).save(
            diff_path.with_name(f"expected-page-{page_label}.png")
        )
        ImageOps.autocontrast(actual).save(
            diff_path.with_name(f"actual-page-{page_label}.png")
        )
        return False

    diff = ImageChops.difference(expected, actual)
    if diff.getbbox() is None:
        return True

    diff_path.parent.mkdir(parents=True, exist_ok=True)
    ImageOps.autocontrast(diff).save(diff_path)
    return False


def _run_fixture_mode(fixture: str, *, mode: str, update: bool) -> int:
    """Run the snapshot test for a fixture and export mode."""
    if mode not in {"latex", "webpdf"}:
        raise ValueError(f"Unknown mode: {mode}")

    notebook = FIXTURES[fixture]
    webpdf = mode == "webpdf"
    artifacts_dir = _artifacts_dir(fixture, mode)

    with tempfile.TemporaryDirectory() as td:
        td_path = Path(td)
        out_pdf = td_path / f"{fixture}.{mode}.pdf"

        try:
            _export_pdf(notebook, out_pdf, webpdf=webpdf)
        except RuntimeError as e:
            msg = str(e)
            lower = msg.lower()

            lines = [msg]
            if "no module named" in lower and ("nbconvert" in lower or "nbformat" in lower):
                lines.extend(
                    [
                        "",
                        "Tip: PDF export requires nbformat and nbconvert. Install Python deps with:",
                        "",
                        "  uv sync --extra pdf",
                    ]
                )

            if mode == "latex" and ("pandoc" in lower or "xelatex" in lower or "texlive" in lower):
                lines.extend(
                    [
                        "",
                        "Tip: LaTeX PDF export requires a TeX distribution + pandoc.",
                        "",
                        "  Ubuntu/Debian: sudo apt-get install texlive-xetex texlive-fonts-recommended "
                        "texlive-plain-generic pandoc",
                        "  macOS: brew install --cask mactex && brew install pandoc",
                    ]
                )

            if webpdf and ("playwright" in lower or "chromium" in lower):
                lines.extend(
                    [
                        "",
                        "Tip: WebPDF export requires Chromium. Install it with:",
                        "",
                        "  uv run python -m playwright install chromium",
                    ]
                )

            raise RuntimeError("\n".join(lines)) from None

        page_count = _pdf_page_count(out_pdf)
        width = max(2, len(str(page_count)))
        pages = range(1, page_count + 1)

        if update:
            for page in pages:
                label = _page_label(page, width=width)
                out_png = td_path / f"page-{label}.png"
                _rasterize_page(out_pdf, out_png, page=page)

                rendered = Image.open(out_png).convert("RGBA")
                rendered = _normalize_image(mode, rendered, pdf_path=out_pdf, page=page)

                baseline = _baseline_path(fixture, mode, label)
                baseline.parent.mkdir(parents=True, exist_ok=True)
                rendered.save(baseline)
            print(f"✅ Updated baseline(s) ({fixture}/{mode}).")
            return 0

        missing: list[Path] = []
        for page in pages:
            label = _page_label(page, width=width)
            baseline = _baseline_path(fixture, mode, label)
            if not baseline.exists():
                missing.append(baseline)

        if missing:
            print(f"❌ Missing baseline(s) ({fixture}/{mode}):")
            for baseline in missing:
                print(f"   - {baseline.relative_to(REPO_ROOT)}")
            print("   Tip: run `uv run scripts/test_pdf_visual_snapshots.py --update`")
            return 2

        if artifacts_dir.exists():
            shutil.rmtree(artifacts_dir)
        artifacts_dir.mkdir(parents=True, exist_ok=True)

        ok_all = True
        mismatches: list[str] = []
        for page in pages:
            label = _page_label(page, width=width)
            out_png = td_path / f"page-{label}.png"
            _rasterize_page(out_pdf, out_png, page=page)

            rendered = Image.open(out_png).convert("RGBA")
            rendered = _normalize_image(mode, rendered, pdf_path=out_pdf, page=page)

            baseline = _baseline_path(fixture, mode, label)
            expected = Image.open(baseline).convert("RGBA")
            expected = _normalize_image(mode, expected, pdf_path=out_pdf, page=page)

            actual_saved = artifacts_dir / f"actual-page-{label}.png"
            diff_saved = artifacts_dir / f"diff-page-{label}.png"
            rendered.save(actual_saved)

            ok = _compare_images(expected, rendered, diff_saved, page_label=label)
            if not ok:
                mismatches.append(label)
            ok_all = ok_all and ok

        if ok_all:
            shutil.rmtree(artifacts_dir)
            print(f"✅ PDF visual snapshot matched ({fixture}/{mode}).")
            return 0

        print(f"❌ PDF visual snapshot mismatch ({fixture}/{mode}) on page(s): {mismatches}")
        print(f"   Artifacts: {artifacts_dir.relative_to(REPO_ROOT)}")
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
    parser.add_argument(
        "--fixture",
        action="append",
        choices=sorted(FIXTURES.keys()),
        help="Which fixture(s) to test. Repeatable. Defaults to all.",
    )
    args = parser.parse_args()

    modes = args.mode or ["latex", "webpdf"]
    fixtures = args.fixture or list(FIXTURES.keys())

    exit_code = 0
    for fixture in fixtures:
        for mode in modes:
            exit_code = max(
                exit_code, _run_fixture_mode(fixture, mode=mode, update=args.update)
            )
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
