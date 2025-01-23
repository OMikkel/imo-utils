from rich.console import Console
from rich.table import Table
from sympy import Matrix as sp_Matrix, diff as sp_diff, Symbol as sp_Symbol, sympify as sp_sympify
from numpy import array as np_array, eye as np_eye, copy as np_copy, matmul as np_matmul
from fractions import Fraction

console = Console()

def compute_gradient(function, variables, datatype):
    gradient = sp_Matrix([sp_diff(function, var) for var in variables])
    gradient = np_array(gradient.tolist(), dtype=datatype)
    return gradient

def compute_hessian(function, variables, datatype):
    n = len(variables)
    hessian = sp_Matrix(n, n, lambda i, j: sp_diff(sp_diff(function, variables[i]), variables[j]))
    hessian = np_array(hessian.tolist(), dtype=datatype)
    return hessian

def compute_diagonal_hessian(matrix):
    B = np_eye(len(matrix))
    A = np_copy(matrix)

    for i in range(0, len(matrix)):

        for j in range(i+1, len(matrix)):
            B[i][j] = -(A[i][j]/A[i][i])

        result = np_matmul(B[i:, i:].T, A[i:, i:])
        result = np_matmul(result, B[i:, i:])
        
        A[i:, i:] = result

    return (A,B)

def compute_hessian_result(matrix):
    diagonal_matrix = compute_diagonal_hessian(matrix)
    diagonal = diagonal_matrix[0].diagonal()

    print_matrix("Hessian Matrix (A)", matrix)
    print_matrix("Final Result (BT*A*B)", diagonal_matrix[0])
    
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

    print_matrix("Final (B)", diagonal_matrix[1])

def eval_variables(variables_str: str):
    try:
        variable_names = variables_str.replace(" ", "").split(",")
        variables = [sp_Symbol(name) for name in variable_names]
    except Exception as e:
        print("[red]Error: Invalid variables[/red]", e)
        return

    return variables

def eval_function(function_str: str, variables: list[sp_Symbol]):
    try:
        return sp_sympify(function_str, locals={var.name: var for var in variables})
    except Exception as e:
        print("[red]Error: Invalid function or variables[/red]", e)
        return

def eval_matrix(matrix_str: str):
    try:
        processed_input = eval(matrix_str, {"__builtins__": None}, {"Fraction": Fraction})
        matrix = np_array(processed_input, dtype=float)
        return matrix
    except Exception as e:
        print("[red]Error: Invalid matrix[/red]", e)
        return

def print_matrix(title, matrix):
    table = Table(title=title, show_header=False, show_lines=True, title_style="green")
    
    for row in matrix:
        table.add_row(*[str(convert_to_fraction(cell)) for cell in row])
    
    console.print("\n", table)

def print_gaussian(title, matrix, variables = []):
    if len(variables) == len(matrix[0])-1:
        column_names = variables
    else:
        column_names = ["x" + str(i) for i in range(1, len(matrix[0]))]

    table = Table("n", *column_names, "=", title=title, show_header=True, show_lines=True, title_style="green")
    
    index = 1
    for row in matrix:
        table.add_row(str(index), *[str(convert_to_fraction(cell)) for cell in row])
        index += 1
    
    console.print("\n", table)

def print_gaussian_solution(matrix, variables = []):
    if len(variables) == len(matrix[0])-1:
        column_names = variables
    else:
        column_names = ["x" + str(i) for i in range(1, len(matrix[0]))]

    table = Table(title="Gaussian Solution", show_lines=True, show_edge=False, title_style="green")
    
    for i in range(0, len(matrix)):
        solution = column_names[i] + " = " + (matrix[i][-1] != 0 and str(convert_to_fraction(matrix[i][-1])) + " " or "")
        for j in range(i+1, len(matrix[0])-1):
            if matrix[i][j] != 0:
                if matrix[i][j] == 1:
                    solution += "- " + column_names[j] + " "
                elif matrix[i][j] == -1:
                    solution += column_names[j] + " "
                else:
                    solution += str(convert_to_fraction(-1*matrix[i][j])) + column_names[j] + " "
        table.add_row(solution)

    console.print("\n", table)

def convert_to_fraction(number):
    try:
        if number % 1 == 0:
            return int(number)
        else:
            fraction = Fraction(number).limit_denominator()
            if fraction.denominator > 100:
                return number
            
            return fraction
    except Exception as e:
        return number

def print(*args, **kwargs):
    console.print(*args, **kwargs)