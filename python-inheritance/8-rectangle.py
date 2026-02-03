#!/usr/bin/python3
"""
Module defining BaseGeometry and Rectangle classes
"""


class BaseGeometry:
    """
    Base class for geometry objects.
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Rectangle class with width and height
    """

    def __init__(self, width, height):
        """
        Constructor for Rectangle

        Args:
            width (int): width of the rectangle, must be positive
            height (int): height of the rectangle, must be positive
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
