#!/usr/bin/python3
"""
Defines a CountedIterator class.
"""


class CountedIterator:
    """
    Iterator that counts the number of items iterated.
    """

    def __init__(self, some_iterable):
        self.iterator = iter(some_iterable)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        return self.count
