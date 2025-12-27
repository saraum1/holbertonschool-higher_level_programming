#!/usr/bin/python3
"""Module that generates Pascal's triangle."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle of n.

    Args:
        n (int): Number of rows.

    Returns:
        list: Triangle rows, or empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            last = triangle[-1]
            for j in range(1, i):
                row.append(last[j - 1] + last[j])
            row.append(1)
        triangle.append(row)
    return triangle
