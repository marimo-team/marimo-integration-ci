
__generated_with = "0.10.7"

# %%
import marimo as mo

# %%
from vega_datasets import data

# %%
explorer = mo.ui.data_explorer(data.iris())
explorer

# %%
explorer.value