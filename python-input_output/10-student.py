#!/usr/bin/python3
"""Module that defines a Student class with JSON export filtering."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dict representation of the instance.

        If attrs is a list of strings, only keys in attrs are returned.
        Otherwise, all attributes are returned.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            result = {}
            for key in attrs:
                if key in self.__dict__:
                    result[key] = self.__dict__[key]
            return result
        return self.__dict__
