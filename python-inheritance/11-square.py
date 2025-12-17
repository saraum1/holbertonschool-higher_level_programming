#!/usr/bin/python3
"""Define Square with custom string description."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square based on Rectangle."""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return area of square."""
        return self.__size ** 2

    def __str__(self):
        """Return description of square."""
        return "[Square] {0}/{0}".format(self.__size)
