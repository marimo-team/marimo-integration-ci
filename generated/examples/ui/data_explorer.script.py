# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "polars==1.17.1",
#     "vega-datasets==0.9.0",
# ]
# ///


__generated_with = "0.17.0"

# %%
import marimo as mo

# %%
from vega_datasets import data

# %%
explorer = mo.ui.data_explorer(data.iris())
explorer

# %%
explorer.value