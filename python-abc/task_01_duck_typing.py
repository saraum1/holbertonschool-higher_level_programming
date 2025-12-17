#!/usr/bin/env python3
"""Shapes with abstract base class and duck typing."""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract shape."""

    @abstractmethod
    def area(self):
        """Return area."""
        raise NotImplementedError

    @abstractmethod
    def perimeter(self):
        """Return perimeter."""
        raise NotImplementedError


class Circle(Shape):
    """Circle shape."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return circle area."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return circle perimeter."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Return rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Return rectangle perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter of a shape-like object (duck typing)."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
