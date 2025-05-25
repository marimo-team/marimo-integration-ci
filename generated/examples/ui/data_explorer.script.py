
__generated_with = "0.13.11"

# %%
import marimo as mo

# %%
from vega_datasets import data

# %%
explorer = mo.ui.data_explorer(data.iris())
explorer

# %%
explorer.value