#!/usr/bin/python3
"""
Module 0-read_file

This module defines a function that reads a UTF-8 text file
and prints its content to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its content.

    Args:
        filename (str): The name of the file to read (default is an empty string).
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        print(content, end="")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
