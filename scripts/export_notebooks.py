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
    """Export a single marimo notebook to markdown."""
    output_path = f"{notebook_path}.md"
    print(f"Exporting {notebook_path} to {output_path}")

    result = subprocess.run(
        ["marimo", "export", "md", notebook_path, "-o", "generated/" + output_path],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(f"Error exporting {notebook_path}:")
        print(result.stderr)
        raise RuntimeError(f"Failed to export {notebook_path}")

def main():
    parser = argparse.ArgumentParser(description="Export marimo notebooks to markdown")
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

    # Process each whitelisted notebook
    for notebook in WHITELISTED_NOTEBOOKS:
        notebook_path = os.path.join(args.examples_dir, notebook)
        if os.path.exists(notebook_path):
            export_markdown(notebook_path)
        else:
            print(f"Warning: Notebook not found: {notebook_path}")

if __name__ == "__main__":
    main()
