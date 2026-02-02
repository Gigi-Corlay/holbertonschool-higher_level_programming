#!/usr/bin/python3
"""
Module containing the BaseGeometry class.

This module defines an empty class BaseGeometry that can be used
as a base class for other geometry-related classes.
"""


class BaseGeometry:
    """
    Raises an exception because area is not implemented.
    """
    def area(self):
        raise Exception("area() is not implemented")
