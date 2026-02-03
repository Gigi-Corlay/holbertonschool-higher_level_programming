#!/usr/bin/python3

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class for all animals.
    Enforces that all subclasses implement the 'sound' method.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by all subclasses.
        """
        pass


class Dog(Animal):
    """
    Dog class inherits from Animal and implements the 'sound' method.
    """
    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Cat class inherits from Animal and implements the 'sound' method.
    """
    def sound(self):
        return "Meow"
