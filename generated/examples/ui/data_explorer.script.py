
__generated_with = "0.19.4"

# %%
import marimo as mo

# %%
from vega_datasets import data

# %%
explorer = mo.ui.data_explorer(data.iris())
explorer

# %%
explorer.value