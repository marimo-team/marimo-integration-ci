
__generated_with = "0.13.10"

# %%
import marimo as mo

# %%
tabs = mo.ui.tabs({
    "Bob says": mo.md("Hello, Alice! 👋"),
    "Alice says": mo.md("Hello, Bob! 👋")
})
tabs

# %%
tabs.value