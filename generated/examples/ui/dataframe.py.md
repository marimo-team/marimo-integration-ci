---
title: Dataframe.Py
marimo-version: 0.13.10
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

```python {.marimo}
dataframe_transformer = mo.ui.dataframe(data.iris())
dataframe_transformer
```

```python {.marimo}
dataframe_transformer.value
```