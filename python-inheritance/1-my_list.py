#!/usr/bin/python3
"""Define MyList that extends list."""


class MyList(list):
    """MyList prints a sorted version of itself."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
