#!/usr/bin/python3
"""Max integer module."""
def max_integer(list=[]):
    """Return the max integer in a list."""
    if len(list) == 0:
        return None
    max_v = list[0]
    for x in list[1:]:
        if x > max_v:
            max_v = x
    return max_v
