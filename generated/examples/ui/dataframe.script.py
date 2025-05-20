
__generated_with = "0.13.10"

# %%
import marimo as mo

# %%
from vega_datasets import data

# %%
dataframe_transformer = mo.ui.dataframe(data.iris())
dataframe_transformer

# %%
dataframe_transformer.value