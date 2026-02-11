#!/usr/bin/python3
"""
Module 0-read_file

This module defines a function that reads a UTF-8 text file
and prints its content to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its content.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
