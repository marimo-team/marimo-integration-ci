#!/usr/bin/env python3

import argparse
import os
import subprocess

# List of whitelisted notebooks to process
WHITELISTED_NOTEBOOKS: list[str] = [
    "ui/arrays_and_dicts.py",
    "ui/batch_and_form.py",
    "ui/data_explorer.py",
    "ui/filterable_table.py",
    "ui/inputs.py",
    "ui/layout.py",
    "ui/mermaid.py",
    "ui/reactive_plots.py",
    "ui/refresh.py",
    "ui/table.py",
    "ui/tabs.py",
    "ui/task_list.py",
]


def export_markdown(notebook_path: str) -> None:
    """Export a single marimo notebook to markdown format."""
    output_path = f"{notebook_path}.md"
    print(f"Exporting {notebook_path} to {output_path}")

    result = subprocess.run(
        ["marimo", "export", "md", notebook_path, "-o", f"generated/{output_path}"],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(f"Error exporting {notebook_path}:")
        print(result.stderr)
        raise RuntimeError(f"Failed to export {notebook_path}")


def export_html(notebook_path: str) -> None:
    """Export a single marimo notebook to HTML format."""
    ext = "html"
    output_path = f"{notebook_path}.{ext}"
    print(f"Exporting {notebook_path} to {output_path}")
    result = subprocess.run(
        ["marimo", "export", "html", notebook_path, "-o", f"public/{output_path}"],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(f"Error exporting {notebook_path}:")
        print(result.stderr)


def export_html_wasm(notebook_path: str) -> None:
    """Export a single marimo notebook to HTML format."""
    output_path = f"{notebook_path}.wasm.run.html"
    print(f"Exporting {notebook_path} to {output_path}")
    result = subprocess.run(
        [
            "marimo",
            "export",
            "html-wasm",
            notebook_path,
            "-o",
            f"public/{output_path}",
            "--mode",
            "run",
            "--no-show-code",
        ],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(f"Error exporting {notebook_path}:")
        print(result.stderr)

    output_path = f"{notebook_path}.wasm.edit.html"
    print(f"Exporting {notebook_path} to {output_path}")
    result = subprocess.run(
        [
            "marimo",
            "export",
            "html-wasm",
            notebook_path,
            "-o",
            f"public/{output_path}",
            "--mode",
            "edit",
        ],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(f"Error exporting {notebook_path}:")
        print(result.stderr)


def export_ipynb(notebook_path: str) -> None:
    """Export a single marimo notebook to ipynb format."""
    output_path = f"{notebook_path}.ipynb"
    print(f"Exporting {notebook_path} to {output_path}")

    result = subprocess.run(
        [
            "marimo",
            "export",
            "ipynb",
            notebook_path,
            "-o",
            f"generated/{output_path}",
            "--sort",
            "top-down",
            "--include-outputs",
        ],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(f"Error exporting {notebook_path}:")
        print(result.stderr)


def export_script(notebook_path: str) -> None:
    """Export a single marimo notebook to a python script."""
    output_path = f"{notebook_path.replace('.py', '.script.py')}"
    print(f"Exporting {notebook_path} to {output_path}")

    result = subprocess.run(
        ["marimo", "export", "script", notebook_path, "-o", f"generated/{output_path}"],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(f"Error exporting {notebook_path}:")
        print(result.stderr)
        raise RuntimeError(f"Failed to export {notebook_path}")


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
  <body class="font-sans max-w-2xl mx-auto p-8 leading-relaxed">
    <h1 class="mb-8">Marimo Examples</h1>
    <div class="grid gap-4">
"""
        )
        for notebook in WHITELISTED_NOTEBOOKS:
            notebook_name = notebook.split("/")[-1].replace(".py", "")
            display_name = notebook_name.replace("_", " ").title()

            # Static HTML
            f.write(
                f'      <div class="p-4 border border-gray-200 rounded">\n'
                f'        <h3 class="text-lg font-semibold mb-2">{display_name}</h3>\n'
                f'        <div class="flex gap-2">\n'
                f'          <a href="{os.path.join(dir, notebook)}.html" class="px-3 py-1 bg-gray-100 hover:bg-gray-200 rounded">Static HTML</a>\n'
                f'          <a href="{os.path.join(dir, notebook)}.wasm.run.html" class="px-3 py-1 bg-gray-100 hover:bg-gray-200 rounded">WASM Run</a>\n'
                f'          <a href="{os.path.join(dir, notebook)}.wasm.edit.html" class="px-3 py-1 bg-gray-100 hover:bg-gray-200 rounded">WASM Edit</a>\n'
                f"        </div>\n"
                f"      </div>\n"
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
    args = parser.parse_args()

    # Ensure examples directory exists
    if not os.path.exists(args.examples_dir):
        raise FileNotFoundError(f"Examples directory not found: {args.examples_dir}")

    generate_index(args.examples_dir)

    # Process each whitelisted notebook
    for notebook in WHITELISTED_NOTEBOOKS:
        notebook_path = os.path.join(args.examples_dir, notebook)
        if os.path.exists(notebook_path):
            export_markdown(notebook_path)
            export_html(notebook_path)
            export_html_wasm(notebook_path)
            export_ipynb(notebook_path)
            export_script(notebook_path)
        else:
            print(f"Warning: Notebook not found: {notebook_path}")


if __name__ == "__main__":
    main()
