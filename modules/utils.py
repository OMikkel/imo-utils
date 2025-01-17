import numpy as np
import sympy as sp
from rich.console import Console
from rich.table import Table

console = Console()

def compute_hessian(function, variables, datatype):
    n = len(variables)
    hessian = sp.Matrix(n, n, lambda i, j: sp.diff(sp.diff(function, variables[i]), variables[j]))
    hessian = np.array(hessian.tolist(), dtype=datatype)
    return hessian

def compute_diagonal_hessian(matrix):
    B = np.eye(len(matrix))
    A = np.copy(matrix)

    for i in range(0, len(matrix)):

        for j in range(i+1, len(matrix)):
            B[i][j] = -(A[i][j]/A[i][i])

        result = np.matmul(B[i:, i:].T, A[i:, i:])
        result = np.matmul(result, B[i:, i:])
        
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
    
    console.print("\n", table, "\n")