#!/usr/bin/python3
"""
Module that provides a function to write an object
to a text file using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file using JSON representation.

    Args:
        my_obj (any): The Python object to serialize to JSON.
        filename (str): The file in which to write the JSON data.

    Returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
