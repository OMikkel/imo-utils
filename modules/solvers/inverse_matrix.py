import numpy as np
from modules.utils import print_matrix

def inverse_matrix(matrix_str: str):
    try:
        matrix = np.array(eval(matrix_str))
        inverse_matrix = np.linalg.inv(matrix)

        print_matrix("Matrix", matrix)
        print_matrix("Inverse Matrix", inverse_matrix)

    except Exception as e:
        print("[red]Error: Invalid matrix[/red]", e)
        return