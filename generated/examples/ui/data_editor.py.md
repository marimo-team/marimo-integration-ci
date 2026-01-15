---
title: Data Editor
marimo-version: 0.19.2
width: medium
---

```python {.marimo}
import marimo as mo
```

```python {.marimo}
import os
```

```python {.marimo}
DATA_FILE = "data.csv"
```

```python {.marimo}
import polars as pl

if not os.path.exists(DATA_FILE):
    from vega_datasets import data

    data.cars().to_csv(DATA_FILE)

editor = mo.ui.data_editor(pl.read_csv(DATA_FILE)).form(bordered=False)
editor
```

The following cell writes the updated dataframe to disk when the submit button is clicked.

```python {.marimo}
mo.stop(editor.value is None, mo.md("Submit your changes."))

editor.value.write_csv(DATA_FILE)
```