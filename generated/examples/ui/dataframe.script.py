
__generated_with = "0.19.2"

# %%
import marimo as mo

# %%
from vega_datasets import data

# %%
lazy_button = mo.ui.checkbox(label="Lazy Dataframe")
lazy_button

# %%
def format_length(value: float) -> str:
    return f"{value:.1f} cm"

dataframe_transformer = mo.ui.dataframe(
    data.iris(),
    lazy=lazy_button.value,
    format_mapping={
        "sepal_length": format_length,
        "sepal_width": "{:.1f}".format,
    },
)
dataframe_transformer

# %%
dataframe_transformer.value