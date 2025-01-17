from rich.console import Console
from rich.table import Table
from sympy import Matrix as sp_Matrix, diff as sp_diff
from numpy import array as np_array, eye as np_eye, copy as np_copy, matmul as np_matmul

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

def print_matrix(title, matrix):
    table = Table(title=title, show_header=False, show_lines=True, title_style="green")
    
    for row in matrix:
        table.add_row(*[str(cell) for cell in row])
    
    console.print("\n", table)

def print(*args, **kwargs):
    console.print(*args, **kwargs)