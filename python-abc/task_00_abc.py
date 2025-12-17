#!/usr/bin/env python3
"""Abstract animal class and concrete subclasses."""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract animal."""

    @abstractmethod
    def sound(self):
        """Return the animal sound."""
        raise NotImplementedError


class Dog(Animal):
    """Dog animal."""

    def sound(self):
        """Return dog sound."""
        return "Bark"


class Cat(Animal):
    """Cat animal."""

    def sound(self):
        """Return cat sound."""
        return "Meow"
