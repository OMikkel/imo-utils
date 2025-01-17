from modules.utils import compute_hessian, print_matrix, compute_hessian_result
import sympy as sp
import numpy as np
import typer
from rich import print

def hessian_fnc(function_str: str, variables_str: str):
    variable_names = variables_str.replace(" ", "").split(",")
    variables = [sp.Symbol(name) for name in variable_names]

    try:
        function = sp.sympify(function_str, locals={var.name: var for var in variables})
    except Exception as e:
        print("[red]Error: Invalid function or variables[/red]", e)
        return
    
    try:
        hessian_matrix = compute_hessian(function, variables, datatype=float)

        compute_hessian_result(hessian_matrix)
    except Exception as e:
        hessian_matrix = compute_hessian(function, variables, datatype=object)

        print_matrix("Hessian Matrix (A)", hessian_matrix)
        print("[red]Hessian matrix is not a float matrix, could not calculate the final result[/red]")
        

def hessian(matrix_str: str):
    try:
        matrix = np.array(eval(matrix_str))

        compute_hessian_result(matrix)
    except Exception as e:
        print("[red]Error: Invalid matrix[/red]", e)
        return
    



    