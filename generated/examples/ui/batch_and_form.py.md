---
title: Batch And Form
marimo-version: 0.9.33
---

# Batch and Form
<!---->
Make custom UI elements using `batch()`, and turn any UI element
into a form with `form()`.

```{.python.marimo}
reset

variables = (
    mo.md(
        """
        Choose your variable values

        {x}

        {y}
        """
    )
    .batch(
        x=mo.ui.slider(start=1, stop=10, step=1, label="$x =$"),
        y=mo.ui.slider(start=1, stop=10, step=1, label="$y =$"),
    )
    .form(show_clear_button=True, bordered=False)
)

variables
```

```{.python.marimo}
if variables.value is not None:
    submitted_values["x"].add(variables.value["x"])
    submitted_values["y"].add(variables.value["y"])

x = variables.value["x"] if variables.value else "\ldots"
y = variables.value["y"] if variables.value else "\ldots"


mo.md(
    f"""
    At the moment,
    $x = {x}$ and $y = {y}$

    All values ever assumed by $x$ and $y$ are

    {mo.hstack([mo.tree(submitted_values), reset], align="center", gap=4)}
    """
).callout()
```

```{.python.marimo}
reset

submitted_values = {"x": set(), "y": set()}
```

```{.python.marimo}
reset = mo.ui.button(label="reset history")
```

```{.python.marimo}
import marimo as mo
```