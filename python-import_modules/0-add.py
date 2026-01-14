#!/usr/bin/python3
"""
    This program imports the add function from add_0.py
    and prints the sum of 1 and 2
"""
from add_0 import add

if __name__ == "__main__":
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
