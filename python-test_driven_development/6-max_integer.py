#!/usr/bin/python3
"""Module to find the max integer in a list."""

def max_integer(list=[]):
    """Returns the max integer in a list or None if list is empty."""
    if len(list) == 0:
        return None
    max_val = list[0]
    for num in list:
        if num > max_val:
            max_val = num
    return max_val
