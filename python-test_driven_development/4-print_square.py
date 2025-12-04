#!/usr/bin/python3
"""Module that provides print_square function.

This module defines a function that prints a square of '#'.
It validates the size argument before printing.
"""


def print_square(size):
    """Print a square of '#' characters of given size.

    Size must be a non-negative integer.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
