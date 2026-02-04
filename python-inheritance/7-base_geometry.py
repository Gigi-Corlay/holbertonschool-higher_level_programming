#!/usr/bin/python3
"""
Defines a BaseGeometry class.
"""


class BaseGeometry:
    """
    Base class for geometry.
    """

    def area(self):
        """
        Raises an exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates an integer.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
