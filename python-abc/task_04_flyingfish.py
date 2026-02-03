#!/usr/bin/python3
"""
Module to demonstrate multiple inheritance with a FlyingFish class.
FlyingFish inherits from both Fish and Bird, overriding methods
to show multiple inheritance and method resolution order (MRO).
"""


class Fish:
    """
    Parent class representing a fish.
    """

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")


class Bird:
    """
    Parent class representing a bird.
    """
    def fly(self):
        print("The flying fish is soaring!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")


class FlyingFish(Fish, Bird):
    """
    Child class that inherits from Fish and Bird.
    Demonstrates multiple inheritance and method overriding.
    """
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")



    if __name__ == "__main__":
        ff = FlyingFish()

        ff.fly()
        ff.swim()
        ff.habitat()

        print(FlyingFish.mro())
