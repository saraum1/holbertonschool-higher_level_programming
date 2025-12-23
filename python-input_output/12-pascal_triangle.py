#!/usr/bin/python3
"""Module that provides a function to generate Pascal's triangle."""


def pascal_triangle(n):
    """Return a list of lists of integers representing Pascal's triangle of n."""
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            prev = triangle[-1]
            for j in range(1, i):
                row.append(prev[j - 1] + prev[j])
            row.append(1)
        triangle.append(row)
    return triangle
