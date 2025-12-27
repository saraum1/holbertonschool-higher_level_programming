#!/usr/bin/python3
"""Module for converting a class instance to JSON-serializable dict."""


def class_to_json(obj):
    """Return the dictionary description of an object."""
    return obj.__dict__
