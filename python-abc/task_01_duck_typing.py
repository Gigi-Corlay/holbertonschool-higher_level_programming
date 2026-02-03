#!/usr/bin/python3

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class for all shapes.
    Forces subclasses to implement the 'area' method.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        Must be implemented by all subclasses.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Optional method for perimeter.
        Can be overridden by subclasses if needed.
        """
        pass


class Circle(Shape):
    """
    Circle shape that inherits from Shape.
    Implements area and perimeter methods.
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle shape that inherits from Shape.
    Implements area and perimeter methods.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.height + self.width)


def shape_info(shape):
    """
    Accepts any object that behaves like a Shape (duck typing)
    and prints its area and perimeter.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


if __name__ == "__main__":
    c = Circle(5)
    r = Rectangle(4, 7)

    shape_info(c)
    shape_info(r)
