import typer
import sympy as sp
import numpy as np
from modules.solvers.hessian import hessian_fnc, hessian
from modules.solvers.inverse_matrix import inverse_matrix

app = typer.Typer()

@app.command()
def gradient(function: str):
    typer.echo(f"Hello {function}!")

app.command()(hessian_fnc)
app.command()(hessian)
app.command()(inverse_matrix)


if __name__ == "__main__":
    app()