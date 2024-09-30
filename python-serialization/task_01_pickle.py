#!/usr/bin/python3
"""
Contain serialize and deserialize functions
"""
from pickle import load, dump


class CustomObject:
    """
    CustomObject class
    """
    def __init__(self, name, age, is_student):
        """
        CustomObject class constructor
        """
        self.__name = name
        self.__age = age
        self.__is_student = is_student

    def display(self):
        """
        View all attributs of object
        """
        print("Name: {}".format(self.__name))
        print("Age: {}".format(self.__age))
        print("Is Student: {}".format(self.__is_student))

    def serialize(self, filename):
        """
        Serialize object
        """
        try:
            with open(filename, "wb") as f:
                dump(self, f)
        except Exception as e:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize object from file
        """
        try:
            with open(filename, "rb") as f:
                return load(f)
        except Exception as e:
            return None
