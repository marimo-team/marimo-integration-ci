---
title: Table.Py
marimo-version: 0.13.10
---

```python {.marimo}
import marimo as mo
```

```python {.marimo}
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
```

```python {.marimo}
table.value
```