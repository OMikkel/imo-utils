import typer
import sympy as sp
import numpy as np
from modules.utils import compute_hessian, compute_diagonal_hessian
from modules.solvers.hessian import hessian

app = typer.Typer()

@app.command()
def gradient(function: str):
    typer.echo(f"Hello {function}!")

app.command()(hessian)


if __name__ == "__main__":
    app()