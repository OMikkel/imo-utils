from modules.utils import compute_hessian, compute_diagonal_hessian, print_hessian
import sympy as sp
import numpy as np
import typer
from rich import print

def hessian(function_str: str, variables_str: str):
    variable_names = variables_str.replace(" ", "").split(",")
    variables = [sp.Symbol(name) for name in variable_names]

    try:
        function = sp.sympify(function_str, locals={var.name: var for var in variables})
    except Exception as e:
        typer.echo("Error: Invalid function or variables", e)
        return
    
    try:
        hessian_matrix = compute_hessian(function, variables, datatype=float)

        diagonal_matrix = compute_diagonal_hessian(hessian_matrix)
        diagonal = diagonal_matrix[0].diagonal()

        print_hessian("Hessian Matrix (A)", hessian_matrix)
        print_hessian("Final Result (BT*A*B)", diagonal_matrix[0])
        
        if all(diagonal > 0):
            print("[blue]The matrix is positive definite[/blue]")
        elif all(diagonal >= 0):
            print("[blue]The matrix is positive semidefinite[/blue]")
        elif all(diagonal < 0):
            print("[blue]The matrix is negative definite[/blue]")
        elif all(diagonal <= 0):
            print("[blue]The matrix is negative semidefinite[/blue]")
        else:
            print("[blue]The matrix is indefinite[/blue]")

        print_hessian("Final (B)", diagonal_matrix[1])

        
        

    except Exception as e:
        hessian_matrix = compute_hessian(function, variables, datatype=object)

        print_hessian("Hessian Matrix (A)", hessian_matrix)
        print("[red]Hessian matrix is not a float matrix, could not calculate the final result[/red]")
        


    