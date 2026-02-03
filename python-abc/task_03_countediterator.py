#!/usr/bin/python3

class CountedIterator:
    def __init__(self, some_iterable):
        self.iterator = iter(some_iterable)
        self.count = 0

    def get_count(self):
        """
        Return the number of items iterated so far.
        """
        return self.count

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        item = next(self.iterator)
        return item
