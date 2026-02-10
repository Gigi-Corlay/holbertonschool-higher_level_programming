#!/usr/bin/python3

import pickle


class CustomObject:
    """
    Class that represents a custom object with serialization capabilities.
    """
    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.

        Args:
            name (str): Name of the person.
            age (int): Age of the person.
            is_student (bool): True if the person is a student, else False.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the attributes of the object in the specified format.
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serialize the current object to a file using pickle.

        Args:
            filename (str): The name of the file where the object will be saved.

        Returns:
            None if an exception occurs.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a CustomObject from a file using pickle.

        Args:
            filename (str): The name of the file to read the object from.

        Returns:
            CustomObject instance if successful, None if an exception occurs.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                return obj
        except Exception:
            return None
