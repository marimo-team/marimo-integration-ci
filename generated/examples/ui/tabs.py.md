---
title: Tabs
marimo-version: 0.19.4
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