
__generated_with = "0.13.10"

# %%
import marimo as mo

# %%
# ui.table accepts a list of rows as dicts, or a dict mapping column names to values,
# or a dataframe-like object
table = mo.ui.table(
    [
        {"first_name": "Michael", "last_name": "Scott"},
        {"first_name": "Jim", "last_name": "Halpert"},
        {"first_name": "Pam", "last_name": "Beesly"},
    ]
)
table

# %%
table.value