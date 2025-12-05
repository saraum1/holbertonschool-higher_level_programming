#!/usr/bin/python3
"""Text indentation module."""
def text_indentation(text):
    """Print text with formatting."""
    if type(text) is not str:
        raise TypeError("text must be a string")
    buffer = ""
    for c in text:
        buffer += c
        if c in ".?:":
            print(buffer.strip())
            print()
            buffer = ""
    if buffer.strip():
        print(buffer.strip())
