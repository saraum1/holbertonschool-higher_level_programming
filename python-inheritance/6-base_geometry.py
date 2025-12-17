#!/usr/bin/python3
"""Define BaseGeometry with area method."""


class BaseGeometry:
    """BaseGeometry."""

    def area(self):
        """Raise exception for unimplemented area."""
        raise Exception("area() is not implemented")
