#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for row in matrix:
        row_str = " ".join("{:d}".format(num) for num in row)
        print(row_str)
