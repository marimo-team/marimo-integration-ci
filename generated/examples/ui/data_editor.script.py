
__generated_with = "0.17.0"

# %%
import marimo as mo

# %%
import os

# %%
DATA_FILE = "data.csv"

# %%
import polars as pl

if not os.path.exists(DATA_FILE):
    from vega_datasets import data

    data.cars().to_csv(DATA_FILE)

editor = mo.ui.data_editor(pl.read_csv(DATA_FILE)).form(bordered=False)
editor

# %%
mo.md("""The following cell writes the updated dataframe to disk when the submit button is clicked.""")

# %%
mo.stop(editor.value is None, mo.md("Submit your changes."))

editor.value.write_csv(DATA_FILE)