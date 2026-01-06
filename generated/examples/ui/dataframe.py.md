---
title: Dataframe.Py
marimo-version: 0.18.4
width: medium
header: |-
  # /// script
  # requires-python = ">=3.12"
  # dependencies = [
  #     "marimo",
  #     "vega-datasets==0.9.0",
  # ]
  # ///
---

```python {.marimo}
import marimo as mo
```

```python {.marimo}
from vega_datasets import data
```

```python {.marimo hide_code="true"}
lazy_button = mo.ui.checkbox(label="Lazy Dataframe")
lazy_button
```

```python {.marimo}
dataframe_transformer = mo.ui.dataframe(data.iris(), lazy=lazy_button.value)
dataframe_transformer
```

```python {.marimo}
dataframe_transformer.value
```