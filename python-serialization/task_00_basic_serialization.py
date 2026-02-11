#!/usr/bin/python3

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.

    :param data: Python dictionary to serialize
    :param filename: Name of the JSON file to write into
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load a JSON file and deserialize it into a Python dictionary.

    :param filename: Name of the JSON file to read from
    :return: Python dictionary created from JSON data
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
