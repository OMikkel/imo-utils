from modules.solvers.hessian import hessian_fnc, hessian
from modules.solvers.inverse_matrix import inverse_matrix
from modules.solvers.gradient import gradient
from modules.utils import print, eval_function, eval_variables
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
            matrix_str = args[0]
        except:
            print("[red]Invalid arguments[/red]")
            return
        
        hessian(matrix_str=matrix_str)

    def do_inverse_matrix(self, arg):
        "Computes the inverse of a matrix, takes one argument: matrix as a string \nexample: [[1,2],[3,4]]"
        try:
            args = arg.split()
            matrix_str = args[0]
        except:
            print("[red]Invalid arguments[/red]")
            return
        
        inverse_matrix(matrix_str=matrix_str)

    def do_EOF(self, arg):
        "Exits the program"
        print("[red]Exiting the program ...[/red]")
        return True

if __name__ == "__main__":
    IMOCli().cmdloop()