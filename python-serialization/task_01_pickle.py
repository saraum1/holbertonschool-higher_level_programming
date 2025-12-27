#!/usr/bin/env python3
"""Pickle serialization/deserialization for a custom class."""

import pickle


class CustomObject:
    """Represent a simple custom object with pickle support."""

    def __init__(self, name, age, is_student):
        """Initialize CustomObject."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object attributes in the required format."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the current object to a file using pickle.

        Returns:
            None: Always returns None (per requirements for failures too).
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None
        return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize a CustomObject instance from a pickle file.

        Returns:
            CustomObject|None: Instance if success, otherwise None.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            if not isinstance(obj, cls):
                return None
            return obj
        except Exception:
            return None
