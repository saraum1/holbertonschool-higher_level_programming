#!/usr/bin/python3
"""Matrix division module."""
def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div."""
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_len = None
    new = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if row_len is None:
            row_len = len(row)
        elif len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for x in row:
            if type(x) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_row.append(round(x / div, 2))
        new.append(new_row)
    return new
