#!/usr/bin/python3
"""
Module that provides a function to return the dictionary
description with simple data structure for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary representation of a class instance
    with attributes that are serializable (list, dict, str, int, bool).

    Args:
        obj (any): Instance of a class.

    Returns:
        dict: Dictionary containing all attributes of the instance.
    """
    return obj.__dict__
