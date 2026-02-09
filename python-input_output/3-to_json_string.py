#!/usr/bin/python3
"""
Module that provides a function to convert an object
to its JSON representation (string).
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The Python object to convert to JSON string.

    Returns:
        str: The JSON representation of my_obj.
    """
    json_string = json.dumps(my_obj)
    return json_string
