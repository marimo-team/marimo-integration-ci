
__generated_with = "0.9.30"

# %%
import marimo as mo

# %%
mo.md("""## Vertical Stack: `vstack`""")

# %%
mo.md("""# Stacks""")

# %%
mo.md("""## Horizontal Stack: `hstack`""")

# %%
align = mo.ui.dropdown(
    label="Align", options=["start", "end", "center", "stretch"]
)
justify = mo.ui.dropdown(
    label="Justify",
    options=["start", "center", "end", "space-between", "space-around"],
)
gap = mo.ui.number(label="Gap", start=0, stop=100, value=1)
size = mo.ui.slider(label="Size", start=60, stop=500)
wrap = mo.ui.checkbox(label="Wrap")

mo.md(
    f"""
    **Stack parameters**

    {mo.hstack([align, justify, gap, wrap], gap=0.25)}

    **Boxes {size}**
    """
)

# %%
mo.md("""Use `mo.hstack` and `mo.vstack` to layout outputs in rows and columns.""")

# %%
def create_box(num):
    box_size = size.value + num * 10
    return mo.Html(
        f"<div style='min-width: {box_size}px; min-height: {box_size}px; background-color: orange; text-align: center; line-height: {box_size}px'>{str(num)}</div>"
    )


boxes = [create_box(i) for i in range(1, 5)]

# %%
mo.hstack(
    boxes,
    align=align.value,
    justify=justify.value,
    gap=gap.value,
    wrap=wrap.value,
)

# %%
mo.vstack(
    boxes,
    align=align.value,
    gap=gap.value,
)