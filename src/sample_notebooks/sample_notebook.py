import marimo

__generated_with = "0.15.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import math
    return math, mo


@app.cell
def _(mo):
    x = mo.ui.slider(0, 10)
    x
    return (x,)


@app.cell
def _(math, mo, x):
    mo.md(f"""$e^{ {x.value} } = {math.exp(x.value):0.3f}$""")
    return


if __name__ == "__main__":
    app.run()
