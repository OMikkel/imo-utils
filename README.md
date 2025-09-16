# imo-utils CLI

`imo-utils` is a command-line interface (CLI) tool designed to perform various mathematical computations, particularly focused on linear algebra and calculus. It provides a simple and interactive way to solve systems of linear equations, compute gradients, Hessians, and inverse matrices.

## Functionality

The `imo-utils` CLI offers the following functionalities:

*   **Gradient Calculation:** Computes the gradient of a multi-variable function.
*   **Hessian Calculation:** Computes the Hessian matrix of a multi-variable function or a given matrix.
*   **Inverse Matrix Calculation:** Computes the inverse of a square matrix.
*   **Gaussian Elimination:** Solves a system of linear equations using the Gaussian elimination method.

## Input and Commands

The CLI operates in an interactive shell. Below are the available commands and their expected inputs.

### `gradient`

Computes the gradient of a function.

**Arguments:**

1.  `function`: The mathematical function to be differentiated, provided as a string.
2.  `variables`: A comma-separated string of the variables in the function.

**Example:**

```
(imo) gradient x**2+y**2 x,y
```

### `hessian_fnc`

Computes the Hessian matrix of a function.

**Arguments:**

1.  `function`: The mathematical function, provided as a string.
2.  `variables`: A comma-separated string of the variables in the function.

**Example:**

```
(imo) hessian_fnc x**2+y**2 x,y
```

### `hessian`

Computes the Hessian of a matrix.

**Argument:**

1.  `matrix`: The matrix provided as a string in the format `[[row1_val1,row1_val2],[row2_val1,row2_val2]]`.

**Example:**

```
(imo) hessian [[1,2],[3,4]]
```

### `inverse_matrix`

Computes the inverse of a matrix.

**Argument:**

1.  `matrix`: The matrix provided as a string in the format `[[row1_val1,row1_val2],[row2_val1,row2_val2]]`.

**Example:**

```
(imo) inverse_matrix [[1,2],[3,4]]
```

### `gaussian`

Solves a system of linear equations using Gaussian Elimination.

**Arguments:**

1.  `matrix`: The augmented matrix (with the last column being the constants) as a string.
2.  `variables` (optional): A comma-separated string of the variable names.

**Example:**

```
(imo) gaussian [[1,2,9],[3,4,20]] x,y
```

### `exit`

Exits the `imo-utils` CLI.
