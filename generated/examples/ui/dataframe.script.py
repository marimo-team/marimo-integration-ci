# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "vega-datasets==0.9.0",
# ]
# ///


__generated_with = "0.17.0"

# %%
import marimo as mo

# %%
from vega_datasets import data

# %%
dataframe_transformer = mo.ui.dataframe(data.iris())
dataframe_transformer

# %%
dataframe_transformer.value