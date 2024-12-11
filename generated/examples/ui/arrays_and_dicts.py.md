---
title: Arrays And Dicts
marimo-version: 0.9.34
---

# Arrays and Dictionaries
<!---->
Use `mo.ui.array` and `mo.ui.dictionary` to create UI elements that wrap
other elements.

Because UI elements must be assigned to global variables,
these functions are required when the set of elements to create is not
known until runtime.

```{.python.marimo}
create = mo.ui.button(label="Create new collections")
```

```{.python.marimo}
create.center()
```

UI Elements ...

```{.python.marimo}
create

array = mo.ui.array(
    [mo.ui.text()]
    + [mo.ui.slider(1, 10) for _ in range(0, random.randint(2, 5))],
)
dictionary = mo.ui.dictionary(
    {str(i): mo.ui.slider(1, 10) for i in range(0, random.randint(2, 5))}
)

mo.hstack([array, dictionary], justify="space-around")
```

... and their values

```{.python.marimo}
mo.hstack([array.value, dictionary.value], justify="space-around")
```

Key difference between marimo dict and standard python dict:

The main reason to use `mo.ui.dictionary` is for reactive execution — when you interact with an element in a `mo.ui.dictionary`, all cells that reference the `mo.ui.dictionary` run automatically, just like all other ui elements. When you use a regular dictionary, you don't get this reactivity.

```{.python.marimo hide_code="true"}
create

slider = mo.ui.slider(1, 10, show_value=True)
text = mo.ui.text()
date = mo.ui.date()

mo_d = mo.ui.dictionary(
    {
        "slider": slider,
        "text": text,
        "date": date,
    }
)

py_d = {
    "slider": slider,
    "text": text,
    "date": date,
}

mo.hstack(
    [
        mo.vstack(["marimo dict", mo_d]),
        mo.vstack(["original elements", mo.vstack([slider, text, date])]),
        mo.vstack(["python dict", py_d]),
    ],
    justify="space-around",
)
```

```{.python.marimo hide_code="true"}
mo_d_ref = {k: mo_d[k].value for k in mo_d.value.keys()}
py_d_ref = {k: py_d[k].value for k in py_d.keys()}
mo.hstack(
    [
        mo.vstack(["reference of marimo dict", mo_d_ref]),
        mo.vstack(["reference of python dict", py_d_ref]),
    ],
    justify="space-around",
)
```

Notice that when you interact with the UI elements in the marimo dict, the reference of marimo dict updates automatically. However, when you interact with the elements in the python dict, you need to manually re-run the cell to see the updated values.

```{.python.marimo}
import marimo as mo
import random
```