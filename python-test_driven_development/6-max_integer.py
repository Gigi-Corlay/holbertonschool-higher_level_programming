#!/usr/bin/python3
"""Module to find the max integer in a list."""


def max_integer(list=[]):
    """Function to find and return the max integer in a list.
    Returns None if the list is empty.
    """
    if len(list) == 0:
        return None
    result = list[0]
    for i in list[1:]:
        if i > result:
            result = i
    return result
