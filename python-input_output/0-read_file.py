#!/usr/bin/python3
"""Module that provides a function to read a UTF-8 text file and print it."""


def read_file(filename=""):
    """Read a text file (UTF-8) and print its contents to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
