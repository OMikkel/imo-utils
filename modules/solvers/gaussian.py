from modules.utils import print_gaussian, print_gaussian_solution

def gaussian(A, variables):
    print_gaussian("Gaussian Matrix", A, variables)

    A = compute_echelon_form(A)
    print_gaussian("Echelon Form", A, variables)

    A = compute_reduced_echelon_form(A)
    print_gaussian("Reduced Echelon Form", A, variables)

    print_gaussian_solution(A, variables)

def compute_echelon_form(matrix):
    A = matrix.copy()

    # visit each row
    for n in range(0, len(matrix)):
        pivot = matrix[n][n]
        if pivot == 0:
            # swap rows if pivot is 0
            for i in range(n+1, len(matrix)):
                if matrix[i][n] != 0:
                    current_row = matrix[n].copy()
                    matrix[n] = matrix[i]
                    matrix[i] = current_row
                    break
        
        pivot = matrix[n][n]
        if pivot == 0:
            # if no non-zero pivot left in column
            continue

        # eliminate the elements below the pivot
        for i in range(n+1, len(matrix)):
            if matrix[i][n] == 0:
                continue

            factor = matrix[i][n] / pivot
            # subtract the factor times the pivot row from the current row
            for j in range(n, len(matrix[0])):
                matrix[i][j] -= factor * matrix[n][j]

        # ensure pivot is 1
        if pivot != 1:
            factor = 1 / pivot
            for i in range(n, len(matrix[0])):
                matrix[n][i] *= factor
            pivot = matrix[n][n]


    return matrix

def compute_reduced_echelon_form(matrix):
    A = matrix.copy()

    for n in range(len(matrix)-1, -1, -1):
        pivot = matrix[n][n]
        if pivot == 0:
            continue

        for i in range(n-1, -1, -1):
            factor = matrix[i][n] / pivot
            for j in range(n, len(matrix[0])):
                matrix[i][j] -= factor * matrix[n][j]

    return matrix
