---
title: Dataframe
marimo-version: 0.19.4
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
```

```python {.marimo}
dataframe_transformer.value
```