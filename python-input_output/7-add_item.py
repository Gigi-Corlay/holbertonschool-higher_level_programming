#!/usr/bin/python3
"""
Script that adds all arguments to a Python list
and saves them to a JSON file.
"""

import sys

# Import the required functions from other files
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_json(my_add):
    """
    Adds items from `my_add` to a list stored in add_item.json.

    Args:
        my_add (list): List of elements to add.

    Returns:
        None
    """
    filename = "add_item.json"

    try:
        my_list = load_from_json_file(filename)
    except:
        my_list = []

    for item in my_add:
        my_list.append(item)

    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    add_json(sys.argv[1:])
