# Marimo Integration CI

Automated CI pipeline for validating and exporting [marimo](https://github.com/marimo-team/marimo) example notebooks.

## Features

- Automatically exports whitelisted marimo notebooks:
  - to markdown
  - to HTML
  - to WebAssembly
  - to ipynb
  - to flat script
- Triggers on:
  - Pushes to `main` from this repo
  - Nightly builds
  - Manual triggers

## Adding notebooks

Add notebooks to whitelist in `scripts/export_notebooks.py`

## Usage

The pipeline runs automatically on configured triggers. To run manually:

1. Go to Actions tab
2. Select "Export Notebooks" workflow
3. Click "Run workflow"
