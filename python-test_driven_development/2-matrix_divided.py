#!/usr/bin/python3
"""2-matrix_divided module.

This module provides the function matrix_divided(matrix, div)
that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div.

    Args:
        matrix: list of lists of integers or floats.
        div: number (integer or float), not zero.

    Returns:
        A new matrix with each element divided by div,
        rounded to 2 decimal places.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(msg)
    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(elem / div, 2) for elem in row] for row in matrix]
