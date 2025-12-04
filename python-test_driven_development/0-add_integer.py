#!/usr/bin/python3
"""Module that provides add_integer function.

This module defines a function that adds two integers.
It demonstrates basic type checking and TDD style.
"""


def add_integer(a, b=98):
    """Return the integer sum of a and b.

    Both arguments must be integers or floats.
    Floats are cast to integers before addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
