#!/usr/bin/python3
"""
Module that provides a function to create a Python object
from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Args:
        filename (str): The file containing the JSON data.

    Returns:
        object: The Python object deserialized from JSON.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
