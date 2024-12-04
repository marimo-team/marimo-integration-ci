---
title: Tabs
marimo-version: 0.9.29
---

# Tabs
<!---->
Use `mo.ui.tabs` to organize outputs.

```{.python.marimo}
settings = mo.vstack(
    [
        mo.md("Edit User"),
        first := mo.ui.text(label="First Name"),
        last := mo.ui.text(label="Last Name"),
    ]
)

organization = mo.vstack(
    [
        mo.md("Edit Organization"),
        org := mo.ui.text(label="Organization Name", value="..."),
        employees := mo.ui.number(
            label="Number of Employees", start=0, stop=1000
        ),
    ]
)

mo.ui.tabs(
    {
        "🧙‍♀ User": settings,
        "🏢 Organization": organization,
    }
)
```

```{.python.marimo}
mo.md(
    f"""
    Welcome **{first.value} {last.value}** to **{org.value}**! You are 
    employee no. **{employees.value + 1}**.

    #{"🎉" * (min(employees.value + 1, 1000))} 
    """
) if all([first.value, last.value, org.value]) else None
```

```{.python.marimo}
import marimo as mo
```