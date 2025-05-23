---
title: Filterable Table
marimo-version: 0.9.34
width: medium
---

# Filterable DataFrame

```{.python.marimo}
# Read the csv
df = pd.read_json(data_url("cars.json"))
```

```{.python.marimo}
# Create options for select widgets
manufacturer_options = df["Name"].str.split().str[0].unique()
manufacturer_options.sort()
cylinder_options = df["Cylinders"].unique().astype(str)
cylinder_options.sort()
```

```{.python.marimo}
# Create the filters
manufacturer = mo.ui.dropdown(manufacturer_options, label="Manufacturer")
cylinders = mo.ui.dropdown(cylinder_options, label="Cylinders")

horse_power = mo.ui.range_slider.from_series(
    df["Horsepower"],
    show_value=True,
)

mo.hstack([manufacturer, horse_power, cylinders], gap=3).left()
```

```{.python.marimo}
filter_df(df)
```

```{.python.marimo}
def filter_df(df):
    filtered_df = df
    if manufacturer.value:
        filtered_df = filtered_df[
            filtered_df["Name"].str.contains(manufacturer.value, case=False)
        ]
    if cylinders.value:
        filtered_df = filtered_df[filtered_df["Cylinders"] == cylinders.value]
    if horse_power.value:
        left, right = horse_power.value
        filtered_df = filtered_df[
            (filtered_df["Horsepower"] >= left)
            & (filtered_df["Horsepower"] <= right)
        ]
    return filtered_df
```

```{.python.marimo}
def data_url(file):
    return f"https://cdn.jsdelivr.net/npm/vega-datasets@v1.29.0/data/{file}"
```

```{.python.marimo}
import marimo as mo
import pandas as pd
```