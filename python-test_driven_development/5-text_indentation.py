#!/usr/bin/python3
"""Module that provides text_indentation function.

This module defines a function that prints text with indentation.
It adds two new lines after '.', '?' and ':'.
"""


def text_indentation(text):
    """Print text with two new lines after '.', '?' and ':'.

    Text must be a string and leading spaces after separators are removed.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_line = False
    for char in text:
        if new_line and char == " ":
            continue
        print(char, end="")
        new_line = False
        if char in ".?:":
            print("\n")
            new_line = True
