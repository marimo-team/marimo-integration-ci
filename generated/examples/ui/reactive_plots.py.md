---
title: Reactive Plots
marimo-version: 0.9.34
width: full
---

# Welcome to marimo!

```{.python.marimo}
chart = mo.ui.altair_chart(scatter & bars)
chart
```

```{.python.marimo}
(filtered_data := mo.ui.table(chart.value))
```

```{.python.marimo}
mo.stop(not len(filtered_data.value))
mpg_hist = mo.ui.altair_chart(
    alt.Chart(filtered_data.value)
    .mark_bar()
    .encode(alt.X("Miles_per_Gallon:Q", bin=True), y="count()")
)
horsepower_hist = mo.ui.altair_chart(
    alt.Chart(filtered_data.value)
    .mark_bar()
    .encode(alt.X("Horsepower:Q", bin=True), y="count()")
)
mo.hstack([mpg_hist, horsepower_hist], justify="space-around", widths="equal")
```

```{.python.marimo}
cars = data.cars()
brush = alt.selection_interval()
scatter = (
    alt.Chart(cars)
    .mark_point()
    .encode(
        x="Horsepower",
        y="Miles_per_Gallon",
        color="Origin",
    )
    .add_params(brush)
)
bars = (
    alt.Chart(cars)
    .mark_bar()
    .encode(y="Origin:N", color="Origin:N", x="count(Origin):Q")
    .transform_filter(brush)
)
```

```{.python.marimo}
import altair as alt
from vega_datasets import data
```

```{.python.marimo}
import marimo as mo
```