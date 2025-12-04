#!/usr/bin/python3
"""Module that provides add_integer function.

This module defines a function that adds two integers.
It validates the input types for TDD exercises.
"""


def add_integer(a, b=98):
    """Return the integer sum of a and b.

    Both arguments must be integers or floats.
    Special float values like NaN or infinity are rejected.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        if a != a or a in (float('inf'), float('-inf')):
            raise TypeError("a must be an integer")
    if isinstance(b, float):
        if b != b or b in (float('inf'), float('-inf')):
            raise TypeError("b must be an integer")

    return int(a) + int(b)
