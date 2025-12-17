#!/usr/bin/env python3
"""CountedIterator tracks how many items have been iterated."""


class CountedIterator:
    """Iterator wrapper that counts successful next() calls."""

    def __init__(self, iterable):
        self._iterator = iter(iterable)
        self._count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self._iterator)
        self._count += 1
        return item

    def get_count(self):
        """Return number of items successfully iterated."""
        return self._count
