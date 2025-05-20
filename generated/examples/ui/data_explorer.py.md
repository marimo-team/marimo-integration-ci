---
title: Data Explorer.Py
marimo-version: 0.13.10
width: medium
header: |-
  # /// script
  # requires-python = ">=3.12"
  # dependencies = [
  #     "polars==1.17.1",
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

```python {.marimo}
explorer = mo.ui.data_explorer(data.iris())
explorer
```

```python {.marimo}
explorer.value
```