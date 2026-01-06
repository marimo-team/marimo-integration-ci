# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "vega-datasets==0.9.0",
# ]
# ///


__generated_with = "0.18.4"

# %%
import marimo as mo

# %%
from vega_datasets import data

# %%
lazy_button = mo.ui.checkbox(label="Lazy Dataframe")
lazy_button

# %%
dataframe_transformer = mo.ui.dataframe(data.iris(), lazy=lazy_button.value)
dataframe_transformer

# %%
dataframe_transformer.value