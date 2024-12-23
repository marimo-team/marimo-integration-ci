---
title: Table
marimo-version: 0.9.34
---

# Tables

> “Sometimes I’ll start a sentence and I don’t even know where it’s going. I just hope I find it along the way.”
— Michael Scott
<!---->
_Create rich tables with selectable rows using_ `mo.ui.table`.
<!---->
**Single selection.**

```{.python.marimo}
single_select_table = mo.ui.table(
    office_characters,
    selection="single",
    pagination=True,
)
```

```{.python.marimo}
mo.ui.tabs({"table": single_select_table, "selection": single_select_table.value})
```

**Multi-selection.**

```{.python.marimo}
multi_select_table = mo.ui.table(
    office_characters,
    selection="multi",
    pagination=True,
)
```

```{.python.marimo}
mo.ui.tabs({"table": multi_select_table, "selection": multi_select_table.value})
```

**No selection.**

```{.python.marimo}
table = mo.ui.table(
    office_characters,
    label="Employees",
    selection=None,
)

table
```

```{.python.marimo}
office_characters = [
    {
        "first_name": "Michael",
        "last_name": "Scott",
        "skill": mo.ui.slider(1, 10, value=3),
        "favorite place": mo.image(src="https://picsum.photos/100", rounded=True),
    },
    {
        "first_name": "Jim",
        "last_name": "Halpert",
        "skill": mo.ui.slider(1, 10, value=7),
        "favorite place": mo.image(src="https://picsum.photos/100"),
    },
    {
        "first_name": "Pam",
        "last_name": "Beesly",
        "skill": mo.ui.slider(1, 10, value=3),
        "favorite place": mo.image(src="https://picsum.photos/100"),
    },
    {
        "first_name": "Dwight",
        "last_name": "Schrute",
        "skill": mo.ui.slider(1, 10, value=7),
        "favorite place": mo.image(src="https://picsum.photos/100"),
    },
    {
        "first_name": "Angela",
        "last_name": "Martin",
        "skill": mo.ui.slider(1, 10, value=5),
        "favorite place": mo.image(src="https://picsum.photos/100"),
    },
    {
        "first_name": "Kevin",
        "last_name": "Malone",
        "skill": mo.ui.slider(1, 10, value=3),
        "favorite place": mo.image(src="https://picsum.photos/100"),
    },
    {
        "first_name": "Oscar",
        "last_name": "Martinez",
        "skill": mo.ui.slider(1, 10, value=3),
        "favorite place": mo.image(src="https://picsum.photos/100"),
    },
    {
        "first_name": "Stanley",
        "last_name": "Hudson",
        "skill": mo.ui.slider(1, 10, value=5),
        "favorite place": mo.image(src="https://picsum.photos/100"),
    },
    {
        "first_name": "Phyllis",
        "last_name": "Vance",
        "skill": mo.ui.slider(1, 10, value=5),
        "favorite place": mo.image(src="https://picsum.photos/100"),
    },
    {
        "first_name": "Meredith",
        "last_name": "Palmer",
        "skill": mo.ui.slider(1, 10, value=7),
        "favorite place": mo.image(src="https://picsum.photos/100"),
    },
    {
        "first_name": "Creed",
        "last_name": "Bratton",
        "skill": mo.ui.slider(1, 10, value=3),
        "favorite place": mo.image(src="https://picsum.photos/100"),
    },
    {
        "first_name": "Ryan",
        "last_name": "Howard",
        "skill": mo.ui.slider(1, 10, value=5),
        "favorite place": mo.image(src="https://picsum.photos/100"),
    },
    {
        "first_name": "Kelly",
        "last_name": "Kapoor",
        "skill": mo.ui.slider(1, 10, value=3),
        "favorite place": mo.image(src="https://picsum.photos/100"),
    },
    {
        "first_name": "Toby",
        "last_name": "Flenderson",
        "skill": mo.ui.slider(1, 10, value=3),
        "favorite place": mo.image(src="https://picsum.photos/100"),
    },
    {
        "first_name": "Darryl",
        "last_name": "Philbin",
        "skill": mo.ui.slider(1, 10, value=7),
        "favorite place": mo.image(src="https://picsum.photos/100"),
    },
    {
        "first_name": "Erin",
        "last_name": "Hannon",
        "skill": mo.ui.slider(1, 10, value=5),
        "favorite place": mo.image(src="https://picsum.photos/100"),
    },
    {
        "first_name": "Andy",
        "last_name": "Bernard",
        "skill": mo.ui.slider(1, 10, value=5),
        "favorite place": mo.image(src="https://picsum.photos/100"),
    },
    {
        "first_name": "Jan",
        "last_name": "Levinson",
        "skill": mo.ui.slider(1, 10, value=5),
        "favorite place": mo.image(src="https://picsum.photos/100"),
    },
    {
        "first_name": "David",
        "last_name": "Wallace",
        "skill": mo.ui.slider(1, 10, value=3),
        "favorite place": mo.image(src="https://picsum.photos/100"),
    },
    {
        "first_name": "Holly",
        "last_name": "Flax",
        "skill": mo.ui.slider(1, 10, value=7),
        "favorite place": mo.image(src="https://picsum.photos/100"),
    },
]
```

```{.python.marimo}
import marimo as mo
```