#!/usr/bin/python3
"""Module that exposes a function to prepare an object for JSON."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON serialization."""
    return obj.__dict__
