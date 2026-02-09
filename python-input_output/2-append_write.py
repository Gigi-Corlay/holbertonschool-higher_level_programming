#!/usr/bin/python3
"""
Function that appends a string at the end of a UTF-8 text file
and returns the number of characters written.
"""


def append_write(filename="", text=""):
    """
    Appends `text` to `filename` and returns the number of characters written.

    Args:
        filename (str): The name of the file.
        text (str): The text to append to the file.

    Returns:
        int: Number of characters written.
    """

    with open(filename, "a", encoding="utf-8") as f:
        nb_char = f.write(text)
    return nb_char
