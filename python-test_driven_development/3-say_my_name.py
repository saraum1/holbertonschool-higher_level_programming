#!/usr/bin/python3
"""Module that provides say_my_name function.

This module defines a function that prints a formatted name.
It validates that provided names are strings.
"""


def say_my_name(first_name, last_name=""):
    """Print the full name in the format 'My name is <first> <last>'.

    Both first_name and last_name must be strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
