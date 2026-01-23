#!/usr/bin/python3
"""This module provides a function that prints
a text with indentation rules."""


def text_indentation(text):
    """
    Prints a text with two new lines after each '.', '?' and ':'.
    Removes spaces at the beginning and end of each printed line.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    skip_space = True

    for ch in text:
        if skip_space and ch == " ":
            continue

        skip_space = False

        if ch in ".?:":
            print(line + ch)
            print()
            line = ""
            skip_space = True
        else:
            line += ch

    if line != "":
        print(line, end="")
