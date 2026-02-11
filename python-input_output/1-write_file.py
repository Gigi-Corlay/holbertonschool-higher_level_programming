#!/usr/bin/python3
"""
Module that defines a function to write a string to a UTF-8 text file
and return the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Write a string to a UTF-8 text file and return the number of characters written.

    Args:
        filename (str): Name of the file to write to.
        text (str): The text to write into the file.

    Returns:
        int: Number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
