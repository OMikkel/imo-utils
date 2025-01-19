from sympy import Symbol as sp_Symbol, sympify as sp_sympify
from modules.utils import print, print_matrix, compute_gradient

def gradient(function, variables):
    try:
        gradient = compute_gradient(function, variables, datatype=float)

        print_matrix("Gradient", gradient)
    except Exception as e:
        gradient = compute_gradient(function, variables, datatype=object)

        print_matrix("Gradient", gradient)
    
