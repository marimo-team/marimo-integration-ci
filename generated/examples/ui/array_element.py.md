---
title: Array Element.Py
marimo-version: 0.14.1
width: medium
---

```python {.marimo}
import marimo as mo
```

```python {.marimo}
array = mo.ui.array([mo.ui.text(), mo.ui.slider(1, 10), mo.ui.date()])
array
```

```python {.marimo}
array.value
```