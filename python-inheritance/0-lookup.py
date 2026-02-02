#!/usr/bin/python3
"""
Module that defines a function to list all attributes and methods
of a given object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    """
    return dir(obj)
