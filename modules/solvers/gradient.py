from sympy import Symbol as sp_Symbol, sympify as sp_sympify
from modules.utils import print, print_matrix, compute_gradient

def gradient(function_str: str, variables_str: str):
    variable_names = variables_str.replace(" ", "").split(",")
    variables = [sp_Symbol(name) for name in variable_names]

    try:
        function = sp_sympify(function_str, locals={var.name: var for var in variables})
    except Exception as e:
        print("[red]Error: Invalid function or variables[/red]", e)
        return
    
    try:
        gradient = compute_gradient(function, variables, datatype=float)

        print_matrix("Gradient", gradient)
    except Exception as e:
        gradient = compute_gradient(function, variables, datatype=object)

        print_matrix("Gradient", gradient)
    
