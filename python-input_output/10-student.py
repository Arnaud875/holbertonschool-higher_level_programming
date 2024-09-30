#!/usr/bin/python3
"""
Contain json function
"""


class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        """
        Student constructor method
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Transfrom student object instance to json
        """

        if not type(attrs) is list or not all(type(i) is str for i in attrs):
            return self.__dict__
        return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
