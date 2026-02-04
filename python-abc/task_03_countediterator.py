#!/usr/bin/python3
"""Defines a CountedIterator class."""

class CountedIterator:
    """Iterator that counts the number of items iterated."""

    def __init__(self, some_iterable):
        """Initialize the iterator and counter."""
        self.iterator = iter(some_iterable)
        self.count = 0

    def get_count(self):
        """Return the number of items iterated so far."""
        return self.count

    def __iter__(self):
        """Return the iterator itself."""
        return self

    def __next__(self):
        """Return the next item and increment the counter."""
        self.count += 1
        return next(self.iterator)
