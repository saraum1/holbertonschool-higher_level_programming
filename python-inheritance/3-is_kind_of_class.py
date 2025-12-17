#!/usr/bin/python3
"""Check instance of a class or a subclass."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or its subclasses."""
    return isinstance(obj, a_class)
