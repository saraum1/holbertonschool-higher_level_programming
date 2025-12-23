#!/usr/bin/python3
"""Module that provides a function to return a dict description of an object."""


def class_to_json(obj):
    """Return the dictionary description for JSON serialization of an object."""
    return obj.__dict__.copy()
