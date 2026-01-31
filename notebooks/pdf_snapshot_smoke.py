# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "matplotlib",
# ]
# ///

import marimo

__generated_with = "0.19.7"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo


@app.cell(hide_code=True)
def _():
    import matplotlib as mpl
    mpl.use("Agg")

    import matplotlib.pyplot as plt

    plt.rcParams.update(
        {
            # Keeping this small so that the PDF fits on a single page.
            "figure.figsize": (2.6, 1.4),
            "figure.dpi": 150,
        }
    )

    x = [1, 2, 3]
    y = [1, 4, 9]

    fig, ax = plt.subplots()
    ax.plot(x, y, marker="o")
    ax.set_title("y=x^2")
    fig.tight_layout()
    fig
    return


if __name__ == "__main__":
    app.run()
