#!/usr/bin/python3
"""
Module containing the is_same_class function.
"""


def is_same_class(obj, a_class):
    """
    Check if `obj` is exactly an instance of `a_class`.

    Args:
        obj: Object to check.
        a_class: Class to compare.

    Returns:
        bool: True if obj is exactly of type a_class, else False.
    """
    return type(obj) is a_class
