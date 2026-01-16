#!/usr/bin/env python3
"""Validation tests for exported notebooks."""
import os
import sys
from export_notebooks import WHITELISTED_NOTEBOOKS

def test_file_exists(path: str, description: str) -> bool:
    """Check if a file exists and has content."""
    if not os.path.exists(path):
        print(f"❌ FAIL: {description} - File not found: {path}")
        return False

    size = os.path.getsize(path)
    if size == 0:
        print(f"❌ FAIL: {description} - File is empty: {path}")
        return False

    print(f"✅ PASS: {description} ({size} bytes)")
    return True

def test_html_valid(path: str, description: str) -> bool:
    """Basic validation of HTML files."""
    if not test_file_exists(path, description):
        return False

    with open(path, 'r') as f:
        content = f.read()
        if '<!DOCTYPE html>' not in content:
            print(f"❌ FAIL: {description} - Missing DOCTYPE")
            return False
        if '</html>' not in content:
            print(f"❌ FAIL: {description} - Missing closing html tag")
            return False

    return True

def main():
    """Run all validation tests."""
    failures = 0
    tests = 0

    print("="*60)
    print("Running export validation tests...")
    print("="*60)

    for notebook in WHITELISTED_NOTEBOOKS:
        base_path = f"examples/{notebook}"

        # Test core formats
        tests += 1
        if not test_file_exists(f"generated/{base_path}.md", f"Markdown: {notebook}"):
            failures += 1

        tests += 1
        if not test_html_valid(f"public/{base_path}.html", f"HTML: {notebook}"):
            failures += 1

        tests += 1
        if not test_html_valid(f"public/{base_path}.wasm.run.html", f"WASM Run: {notebook}"):
            failures += 1

        tests += 1
        if not test_html_valid(f"public/{base_path}.wasm.edit.html", f"WASM Edit: {notebook}"):
            failures += 1

        tests += 1
        if not test_file_exists(f"generated/{base_path}.ipynb", f"Jupyter: {notebook}"):
            failures += 1

        tests += 1
        if not test_file_exists(f"generated/{base_path.replace('.py', '.script.py')}", f"Script: {notebook}"):
            failures += 1

        # Test optional PDF formats
        pdf_path = f"generated/{base_path}.pdf"
        if os.path.exists(pdf_path):
            tests += 1
            if not test_file_exists(pdf_path, f"PDF: {notebook}"):
                failures += 1

        webpdf_path = f"generated/{base_path}.webpdf.pdf"
        if os.path.exists(webpdf_path):
            tests += 1
            if not test_file_exists(webpdf_path, f"WebPDF: {notebook}"):
                failures += 1

    # Test index.html
    tests += 1
    if not test_html_valid("public/index.html", "Index page"):
        failures += 1

    print("="*60)
    print(f"Tests run: {tests}")
    print(f"Failures: {failures}")
    print(f"Success rate: {((tests - failures) / tests * 100):.1f}%")
    print("="*60)

    sys.exit(1 if failures > 0 else 0)

if __name__ == "__main__":
    main()
