#!/usr/bin/python3
def matrix_divided(matrix, div):
    # Validate matrix
    if (
        not isinstance(matrix, list)
        or not matrix
        or not all(isinstance(row, list) for row in matrix)
        or not all(
            isinstance(n, (int, float))
            for row in matrix
            for n in row
        )
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    # Validate row sizes
    if len({len(row) for row in matrix}) != 1:
        raise TypeError(
            "Each row of the matrix must have the same size"
        )

    # Validate divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide and round
    return [
        [round(n / div, 2) for n in row]
        for row in matrix
    ]
