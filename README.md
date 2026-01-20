# Marimo Integration CI

Automated CI pipeline for validating and exporting [marimo](https://github.com/marimo-team/marimo) example notebooks.

## Features

- Automatically exports whitelisted marimo notebooks:
  - to markdown
  - to HTML
  - to WebAssembly
  - to ipynb
  - to flat script
  - to PDF (via nbconvert)
  - to WebPDF (via nbconvert)
- Triggers on:
  - Pushes to `main` from this repo
  - Nightly builds
  - Manual triggers

## Setup

This project uses `uv` for dependency management. To set up locally:

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Sync dependencies (including PDF export support)
uv sync --extra pdf
```

### Clone marimo examples

In CI, the workflow clones example notebooks from [marimo-team/marimo](https://github.com/marimo-team/marimo). To mirror this locally:

```bash
# First time: clone marimo examples
uv run scripts/setup_examples.py

# Run the export script
uv run scripts/export_notebooks.py
```

The setup script will:
1. Sparse-clone `marimo-team/marimo` to get the `examples/` folder
2. Copy your local `notebooks/` into `examples/notebooks/`
3. Clean up the cloned repo

After setup, you can re-run exports anytime with `uv run scripts/export_notebooks.py`.

### System Dependencies for PDF Export

PDF and WebPDF exports require system packages:

```bash
# Ubuntu/Debian
sudo apt-get install texlive-xetex texlive-fonts-recommended texlive-plain-generic pandoc

# macOS
brew install --cask mactex
brew install pandoc
```

To skip PDF exports if these aren't available:
```bash
uv run scripts/export_notebooks.py --skip-pdf --skip-webpdf
```

## Adding notebooks

Add notebooks to whitelist in `scripts/export_notebooks.py`

## Usage

The pipeline runs automatically on configured triggers. To run manually:

1. Go to Actions tab
2. Select "Export Notebooks" workflow
3. Click "Run workflow"
