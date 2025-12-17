#!/usr/bin/env python3
"""Mixins and Dragon class."""


class SwimMixin:
    """Provides swim behavior."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Provides fly behavior."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon combines swim and fly behaviors."""

    def roar(self):
        print("The dragon roars!")
