#!/usr/bin/python3
"""Module that defines add_integer for TDD project.

This module provides a simple function to add two numbers
with strict type checking. It is used with doctest-based
tests to practice test-driven development.
"""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Both a and b must be integers or floats that can be
    safely converted to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    try:
        a_int = int(a)
    except (TypeError, ValueError, OverflowError):
        raise TypeError("a must be an integer")

    try:
        b_int = int(b)
    except (TypeError, ValueError, OverflowError):
        raise TypeError("b must be an integer")

    return a_int + b_int
