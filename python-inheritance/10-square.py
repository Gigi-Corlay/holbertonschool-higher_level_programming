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
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Square class inheriting from Rectangle"""

    def __init__(self, size):
        """
        Constructor for Square

        Args:
            size (int): size of the square, must be positive
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns the area of the square
        """
        return self.__size * self.__size

    def __str__(self):
        """
        String representation of the square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
