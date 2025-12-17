#!/usr/bin/python3
"""Define Rectangle with area and string description."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle based on BaseGeometry integer validation."""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return area of rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return description of rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
