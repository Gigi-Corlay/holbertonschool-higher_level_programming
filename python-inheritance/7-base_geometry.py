#!/usr/bin/python3
"""
Module containing the BaseGeometry class.
This module defines a base class for geometry-related objects.
"""


class BaseGeometry:
    """
    Base class for geometry objects.
    """

    def area(self):
        """
        Raises an Exception indicating that the area method
        is not implemented in the base class.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a strictly positive integer.

        Args:
            name (str): the name of the parameter (used in error messages)
            value (int): the value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
