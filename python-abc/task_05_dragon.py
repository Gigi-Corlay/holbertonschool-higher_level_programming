#!/usr/bin/python3
"""
Defines mixins and a Dragon class.
"""


class SwimMixin:
    """
    Mixin class adding swimming ability.
    """

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class adding flying ability.
    """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that can swim, fly, and roar.
    """
    def roar(self):
        print("The dragon roars!")


if __name__ == "__main__":
    draco = Dragon()
    draco.swim()
    draco.fly() 
    draco.roar()
