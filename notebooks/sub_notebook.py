# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo",
# ]
# ///
from __future__ import annotations

import marimo

app = marimo.App()


with app.setup:
    import marimo as mo


@app.cell
def _():
    mo.md("""
    # Sub Notebook

    This is a sub notebook.
    """)
    return


@app.cell
def _():
    mo.ui.button(label="Click me", on_click=lambda: mo.md("Hello, world!"))
    return
