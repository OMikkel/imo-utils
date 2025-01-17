from modules.utils import compute_hessian, print_matrix, compute_hessian_result
from sympy import Symbol as sp_Symbol, sympify as sp_sympify
from modules.utils import print
from numpy import array as np_array

def hessian_fnc(function_str: str, variables_str: str):
    variable_names = variables_str.replace(" ", "").split(",")
    variables = [sp_Symbol(name) for name in variable_names]

    try:
        function = sp_sympify(function_str, locals={var.name: var for var in variables})
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
        matrix = np_array(eval(matrix_str))

        compute_hessian_result(matrix)
    except Exception as e:
        print("[red]Error: Invalid matrix[/red]", e)
        return
    



    