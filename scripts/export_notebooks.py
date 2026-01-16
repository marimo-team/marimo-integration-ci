#!/usr/bin/env python3

import argparse
import os
import subprocess

# List of whitelisted notebooks to process
WHITELISTED_NOTEBOOKS: list[str] = [
    "notebooks/kitchen_sink.py",
    "ui/array_element.py",
    "ui/arrays_and_dicts.py",
    "ui/batch_and_form.py",
    "ui/chat.py",
    "ui/data_explorer.py",
    "ui/data_editor.py",
    "ui/dataframe.py",
    "ui/layout.py",
    "ui/table.py",
    "ui/tabs.py",
]


def export_markdown(notebook_path: str) -> None:
    """Export a single marimo notebook to markdown format."""
    output_path = f"{notebook_path}.md"
    print(f"📝 {notebook_path} -> generated/{output_path}")

    cmd = [
        "marimo",
        "--yes",
        "export",
        "md",
        notebook_path,
        "-o",
        f"generated/{output_path}",
    ]

    process = None
    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate(timeout=10)
        result = subprocess.CompletedProcess(cmd, process.returncode, stdout, stderr)
    except subprocess.TimeoutExpired:
        print(f"❌ {notebook_path}: Timeout after 10s")
        if process:
            process.kill()
        return
    except Exception as e:
        print(f"❌ {notebook_path}: {str(e)}")
        if process:
            process.kill()
        return

    if result.returncode != 0:
        print(f"❌ {notebook_path}: Export failed")
        print(f"Error: {result.stderr}")
    else:
        print(f"✅ {notebook_path}: Exported to markdown")


def export_html(notebook_path: str) -> None:
    """Export a single marimo notebook to HTML format."""
    output_path = f"{notebook_path}.html"
    print(f"🌐 {notebook_path} -> public/{output_path}")

    cmd = [
        "marimo",
        "--yes",
        "export",
        "html",
        notebook_path,
        "-o",
        f"public/{output_path}",
    ]

    process = None
    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate(timeout=10)
        result = subprocess.CompletedProcess(cmd, process.returncode, stdout, stderr)
    except subprocess.TimeoutExpired:
        print(f"❌ {notebook_path}: Timeout after 10s")
        if process:
            process.kill()
        return
    except Exception as e:
        print(f"❌ {notebook_path}: {str(e)}")
        if process:
            process.kill()
        return

    if result.returncode != 0:
        print(f"❌ {notebook_path}: Export failed")
        print(f"Error: {result.stderr}")
    else:
        print(f"✅ {notebook_path}: Exported to HTML")


def export_html_wasm(notebook_path: str) -> None:
    """Export a single marimo notebook to HTML format."""
    # Run mode
    output_path = f"{notebook_path}.wasm.run.html"
    print(f"⚡ {notebook_path} -> public/{output_path} (WASM run)")

    cmd = [
        "marimo",
        "--yes",
        "export",
        "html-wasm",
        notebook_path,
        "-o",
        f"public/{output_path}",
        "--mode",
        "run",
        "--no-show-code",
    ]

    process = None
    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate(timeout=10)
        result = subprocess.CompletedProcess(cmd, process.returncode, stdout, stderr)
    except subprocess.TimeoutExpired:
        print(f"❌ {notebook_path}: Timeout after 10s")
        if process:
            process.kill()
        return
    except Exception as e:
        print(f"❌ {notebook_path}: {str(e)}")
        if process:
            process.kill()
        return

    if result.returncode != 0:
        print(f"❌ {notebook_path}: Export failed")
        print(f"Error: {result.stderr}")
    else:
        print(f"✅ {notebook_path}: Exported to WASM run")

    # Edit mode
    output_path = f"{notebook_path}.wasm.edit.html"
    print(f"⚡ {notebook_path} -> public/{output_path} (WASM edit)")

    cmd = [
        "marimo",
        "--yes",
        "export",
        "html-wasm",
        notebook_path,
        "-o",
        f"public/{output_path}",
        "--mode",
        "edit",
    ]

    process = None
    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate(timeout=10)
        result = subprocess.CompletedProcess(cmd, process.returncode, stdout, stderr)
    except subprocess.TimeoutExpired:
        print(f"❌ {notebook_path}: Timeout after 10s")
        if process:
            process.kill()
        return
    except Exception as e:
        print(f"❌ {notebook_path}: {str(e)}")
        if process:
            process.kill()
        return

    if result.returncode != 0:
        print(f"❌ {notebook_path}: Export failed")
        print(f"Error: {result.stderr}")
    else:
        print(f"✅ {notebook_path}: Exported to WASM edit")


def export_ipynb(notebook_path: str) -> None:
    """Export a single marimo notebook to ipynb format."""
    output_path = f"{notebook_path}.ipynb"
    print(f"📓 {notebook_path} -> generated/{output_path}")

    cmd = [
        "marimo",
        "--yes",
        "export",
        "ipynb",
        notebook_path,
        "-o",
        f"generated/{output_path}",
        "--sort",
        "top-down",
        "--include-outputs",
    ]

    process = None
    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate(timeout=10)
        result = subprocess.CompletedProcess(cmd, process.returncode, stdout, stderr)
    except subprocess.TimeoutExpired:
        print(f"❌ {notebook_path}: Timeout after 10s")
        if process:
            process.kill()
        return
    except Exception as e:
        print(f"❌ {notebook_path}: {str(e)}")
        if process:
            process.kill()
        return

    if result.returncode != 0:
        print(f"❌ {notebook_path}: Export failed")
        print(f"Error: {result.stderr}")
    else:
        print(f"✅ {notebook_path}: Exported to ipynb")


def export_pdf(notebook_path: str) -> None:
    """Export a single marimo notebook to PDF format via ipynb intermediate."""
    ipynb_path = f"generated/{notebook_path}.ipynb"
    output_path = f"{notebook_path}.pdf"
    print(f"📄 {notebook_path} -> generated/{output_path}")

    if not os.path.exists(ipynb_path):
        print(f"❌ {notebook_path}: ipynb file not found at {ipynb_path}")
        return

    # Use absolute paths and let nbconvert add .pdf extension
    abs_ipynb_path = os.path.abspath(ipynb_path)
    abs_output_path = os.path.abspath(f"generated/{notebook_path}")  # No .pdf extension

    cmd = [
        "uvx",
        "--with", "nbconvert",
        "--from", "jupyter-core",
        "jupyter", "nbconvert",
        "--to", "pdf",
        abs_ipynb_path,
        "--output", abs_output_path,
    ]

    process = None
    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate(timeout=30)
        result = subprocess.CompletedProcess(cmd, process.returncode, stdout, stderr)
    except subprocess.TimeoutExpired:
        print(f"❌ {notebook_path}: PDF export timeout after 30s")
        if process:
            process.kill()
        return
    except Exception as e:
        print(f"❌ {notebook_path}: {str(e)}")
        if process:
            process.kill()
        return

    if result.returncode != 0:
        print(f"❌ {notebook_path}: PDF export failed")
        print(f"Error: {result.stderr}")
        if "xelatex" in result.stderr.lower() or "latex" in result.stderr.lower():
            print("  Hint: LaTeX may not be installed. Install texlive-xetex or similar.")
    else:
        print(f"✅ {notebook_path}: Exported to PDF")


def export_webpdf(notebook_path: str) -> None:
    """Export a single marimo notebook to WebPDF format via ipynb intermediate."""
    ipynb_path = f"generated/{notebook_path}.ipynb"
    output_path = f"{notebook_path}.webpdf.pdf"
    print(f"🌐📄 {notebook_path} -> generated/{output_path}")

    if not os.path.exists(ipynb_path):
        print(f"❌ {notebook_path}: ipynb file not found at {ipynb_path}")
        return

    # Use absolute paths and let nbconvert add .pdf extension
    abs_ipynb_path = os.path.abspath(ipynb_path)
    abs_output_path = os.path.abspath(f"generated/{notebook_path}.webpdf")  # No .pdf extension

    cmd = [
        "uvx",
        "--with", "nbconvert[webpdf]",
        "--from", "jupyter-core",
        "jupyter", "nbconvert",
        "--to", "webpdf",
        abs_ipynb_path,
        "--output", abs_output_path,
        "--allow-chromium-download",
    ]

    process = None
    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate(timeout=60)
        result = subprocess.CompletedProcess(cmd, process.returncode, stdout, stderr)
    except subprocess.TimeoutExpired:
        print(f"❌ {notebook_path}: WebPDF export timeout after 60s")
        if process:
            process.kill()
        return
    except Exception as e:
        print(f"❌ {notebook_path}: {str(e)}")
        if process:
            process.kill()
        return

    if result.returncode != 0:
        print(f"❌ {notebook_path}: WebPDF export failed")
        print(f"Error: {result.stderr}")
        if "chromium" in result.stderr.lower():
            print("  Hint: Chromium download may have failed. Check network connectivity.")
    else:
        print(f"✅ {notebook_path}: Exported to WebPDF")


def export_script(notebook_path: str) -> None:
    """Export a single marimo notebook to a python script."""
    output_path = f"{notebook_path.replace('.py', '.script.py')}"
    print(f"📜 {notebook_path} -> generated/{output_path}")

    cmd = [
        "marimo",
        "--yes",
        "export",
        "script",
        notebook_path,
        "-o",
        f"generated/{output_path}",
    ]

    process = None
    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate(timeout=10)
        result = subprocess.CompletedProcess(cmd, process.returncode, stdout, stderr)
    except subprocess.TimeoutExpired:
        print(f"❌ {notebook_path}: Timeout after 10s")
        if process:
            process.kill()
        return
    except Exception as e:
        print(f"❌ {notebook_path}: {str(e)}")
        if process:
            process.kill()
        return

    if result.returncode != 0:
        if "Cannot export a notebook with async code to a flat script" in result.stderr:
            print(f"⚠️ {notebook_path}: Skipping script export (async code)")
            return
        print(f"❌ {notebook_path}: Export failed")
        print(f"Error: {result.stderr}")
    else:
        print(f"✅ {notebook_path}: Exported to script")


def generate_index(dir: str) -> None:
    """Generate the index.html file."""
    print("Generating index.html")

    with open("public/index.html", "w") as f:
        f.write(
            """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Marimo Examples</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
  </head>
  <body class="font-sans max-w-3xl mx-auto p-8 leading-relaxed">
    <h1 class="mb-8">Marimo Examples</h1>
    <div class="grid gap-4">
"""
        )
        for notebook in WHITELISTED_NOTEBOOKS:
            notebook_name = notebook.split("/")[-1].replace(".py", "")
            display_name = notebook_name.replace("_", " ").title()

            f.write(
                f'      <div class="p-4 border border-gray-200 rounded">\n'
                f'        <h3 class="text-lg font-semibold mb-3">{display_name}</h3>\n'
                f'        <div class="mb-2">\n'
                f'          <span class="text-sm font-medium text-gray-600">Interactive:</span>\n'
                f'          <div class="flex gap-2 mt-1">\n'
                f'            <a href="{os.path.join(dir, notebook)}.html" class="px-3 py-1 bg-blue-100 hover:bg-blue-200 rounded text-sm">Static HTML</a>\n'
                f'            <a href="{os.path.join(dir, notebook)}.wasm.run.html" class="px-3 py-1 bg-purple-100 hover:bg-purple-200 rounded text-sm">WASM Run</a>\n'
                f'            <a href="{os.path.join(dir, notebook)}.wasm.edit.html" class="px-3 py-1 bg-purple-100 hover:bg-purple-200 rounded text-sm">WASM Edit</a>\n'
                f'          </div>\n'
                f'        </div>\n'
                f'        <div>\n'
                f'          <span class="text-sm font-medium text-gray-600">Downloads:</span>\n'
                f'          <div class="flex gap-2 mt-1">\n'
                f'            <a href="../generated/{os.path.join(dir, notebook)}.pdf" class="px-3 py-1 bg-red-100 hover:bg-red-200 rounded text-sm" download>PDF</a>\n'
                f'            <a href="../generated/{os.path.join(dir, notebook)}.webpdf.pdf" class="px-3 py-1 bg-orange-100 hover:bg-orange-200 rounded text-sm" download>WebPDF</a>\n'
                f'            <a href="../generated/{os.path.join(dir, notebook)}.ipynb" class="px-3 py-1 bg-green-100 hover:bg-green-200 rounded text-sm" download>Jupyter</a>\n'
                f'          </div>\n'
                f'        </div>\n'
                f'      </div>\n'
            )
        f.write(
            """    </div>
  </body>
</html>"""
        )


def main():
    parser = argparse.ArgumentParser(description="Export marimo notebooks")
    parser.add_argument(
        "--examples-dir",
        type=str,
        default="examples",
        help="Directory containing example notebooks",
    )
    parser.add_argument(
        "--skip-pdf",
        action="store_true",
        help="Skip PDF exports (useful if LaTeX not available)",
    )
    parser.add_argument(
        "--skip-webpdf",
        action="store_true",
        help="Skip WebPDF exports (useful if avoiding Chromium download)",
    )
    args = parser.parse_args()

    if not os.path.exists(args.examples_dir):
        raise FileNotFoundError(f"Examples directory not found: {args.examples_dir}")

    os.makedirs("generated", exist_ok=True)
    os.makedirs("public", exist_ok=True)

    generate_index(args.examples_dir)

    for notebook in WHITELISTED_NOTEBOOKS:
        notebook_path = os.path.join(args.examples_dir, notebook)
        if os.path.exists(notebook_path):
            print(f"\n{'='*60}")
            print(f"Processing: {notebook}")
            print(f"{'='*60}")

            export_markdown(notebook_path)
            export_html(notebook_path)
            export_html_wasm(notebook_path)
            export_ipynb(notebook_path)  # Must run before PDF exports
            export_script(notebook_path)

            if not args.skip_pdf:
                export_pdf(notebook_path)
            if not args.skip_webpdf:
                export_webpdf(notebook_path)
        else:
            print(f"Warning: Notebook not found: {notebook_path}")

    print(f"\n{'='*60}")
    print("Export complete!")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
