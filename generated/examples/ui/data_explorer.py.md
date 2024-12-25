---
title: Data Explorer
marimo-version: 0.10.7
width: medium
---

```{.python.marimo}
import marimo as mo
```

```{.python.marimo}
from vega_datasets import data
```

```{.python.marimo}
explorer = mo.ui.data_explorer(data.iris())
explorer
```

```{.python.marimo}
explorer.value
```