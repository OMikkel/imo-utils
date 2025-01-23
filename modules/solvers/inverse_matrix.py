from numpy.linalg import inv as np_matrix_inv
from numpy import array as np_array
from modules.utils import print_matrix, print

def inverse_matrix(matrix):
    try:
        inverse_matrix = np_matrix_inv(matrix)

        print_matrix("Matrix", matrix)
        print_matrix("Inverse Matrix", inverse_matrix)

    except Exception as e:
        print("[red]Error: Invalid matrix[/red]", e)
        return