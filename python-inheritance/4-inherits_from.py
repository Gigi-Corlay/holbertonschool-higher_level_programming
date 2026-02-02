#!/usr/bin/python3
"""
Module containing the inherits_from function.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherits from a_class.
    """
    obj_class = type(obj)
    if obj_class is a_class:
        return False

    parents_check = list(obj_class.__bases__)

    while parents_check:
        current_parent = parents_check.pop()
        if current_parent == a_class:
            return True
        parents_check.extend(current_parent.__bases__)
    return False
