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

    def to_json(self):
        """
        Transfrom student object instance to json
        """
        return self.__dict__
