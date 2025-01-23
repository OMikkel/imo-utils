from modules.solvers.hessian import hessian_fnc, hessian
from modules.solvers.inverse_matrix import inverse_matrix
from modules.solvers.gradient import gradient
from modules.solvers.gaussian import gaussian
from modules.utils import print, eval_function, eval_variables, eval_matrix
import cmd

class IMOCli(cmd.Cmd):
    intro = "Welcome to the IMO CLI. Type help or ? to list commands.\n"
    prompt = "(imo) "
    file = None

    def do_exit(self, arg):
        "Exits the program"
        print("[red]Exiting the program ...[/red]")
        return True
    
    def do_gradient(self, arg):
        "Computes the gradient of a function, takes two arguments: function and variables \nExample: gradient x**2+y**2 x,y"
        try:
            args = arg.split()

            variables = eval_variables(args[1])
            function = eval_function(args[0], variables)
        except:
            print("[red]Invalid arguments[/red]")
            return
        
        gradient(function, variables)

    def do_hessian_fnc(self, arg):
        "Computes the hessian of a function, takes two arguments: function and variables \nExample: hessian_fnc x**2+y**2 x,y"
        try:
            args = arg.split()

            variables = eval_variables(args[1])
            function = eval_function(args[0], variables)
        except:
            print("[red]Invalid arguments[/red]")
            return
        
        hessian_fnc(function, variables)
    
    def do_hessian(self, arg):
        "Computes the hessian of a matrix, takes one argument: matrix as a string \nexample: [[1,2],[3,4]]"
        try:
            args = arg.split()
            matrix = eval_matrix(args[0])
        except:
            print("[red]Invalid arguments[/red]")
            return
        
        hessian(matrix)

    def do_inverse_matrix(self, arg):
        "Computes the inverse of a matrix, takes one argument: matrix as a string \nexample: [[1,2],[3,4]]"
        try:
            args = arg.split()
            matrix = eval_matrix(args[0])
        except:
            print("[red]Invalid arguments[/red]")
            return
        
        inverse_matrix(matrix)
    
    def do_gaussian(self, arg):
        "Solves a system of linear equations using Gaussian Elimination, takes two argument: matrix with last col being constants, variable names (optional) \nExample: gaussian [[1,2],[3,4]] x,y"
        try:
            args = arg.split()
            A_matrix = eval_matrix(args[0])
            variables = []
            if len(args) > 1:
                variables = args[1].split(",")
        except Exception as e:
            print("[red]Invalid arguments[/red]", e)
            return
        
        gaussian(A_matrix, variables)

    def do_EOF(self, arg):
        "Exits the program"
        print("[red]Exiting the program ...[/red]")
        return True

if __name__ == "__main__":
    IMOCli().cmdloop()