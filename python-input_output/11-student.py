#!/usr/bin/python3
"""
Module that defines a Student class.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): List of attribute names to include.
                                    If None, all attributes are included.

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if isinstance(attrs, list):
            filtered_dict = {}
            for attr in attrs:
                if attr in self.__dict__:
                    filtered_dict[attr] = self.__dict__[attr]
            return filtered_dict

        return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
