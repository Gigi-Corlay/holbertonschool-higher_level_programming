#!/usr/bin/python3
"""
Module that defines a class MyList that inherits from list
and has a method to print a sorted version of the list.
"""
class MyList(list):
    """
    Class that inherits from list and has a method to print a sorted version.
    """

    def print_sorted(self):
        """
        Prints the list sorted in ascending order
        without modifying the original list.
        """
        print(sorted(self))
