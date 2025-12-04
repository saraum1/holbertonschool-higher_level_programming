#!/usr/bin/python3
"""Module that provides matrix_divided function.

This module defines a function that divides all elements of a matrix.
It validates types and sizes before performing the division.
"""


def matrix_divided(matrix, div):
    """Return a new matrix with elements of matrix divided by div.

    Matrix must be a list of lists of ints/floats and rows same size.
    Div must be a non-zero int or float.
    """
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_len = None
    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if row_len is None:
            row_len = len(row)
        elif len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in row] for row in matrix]
