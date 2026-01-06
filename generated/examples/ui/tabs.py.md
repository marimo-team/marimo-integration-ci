---
title: Tabs.Py
marimo-version: 0.18.4
---

```python {.marimo}
import marimo as mo
```

```python {.marimo}
tabs = mo.ui.tabs({
    "Bob says": mo.md("Hello, Alice! 👋"),
    "Alice says": mo.md("Hello, Bob! 👋")
})
tabs
```

```python {.marimo}
tabs.value
```