#!/usr/bin/python3
"""Module for appending text to a file."""


def append_write(filename="", text=""):
    """Append a string at the end of a text file and return char count."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
