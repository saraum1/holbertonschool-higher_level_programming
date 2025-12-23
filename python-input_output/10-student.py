#!/usr/bin/python3
"""Module that defines a Student class with filtered JSON export."""


class Student:
    """Represent a student with basic public attributes."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dict representation; filter keys if attrs is a list of strings."""
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__.copy()
