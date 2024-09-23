#!/usr/bin/python3
"""This file defines a Square class that inherits
from the Rectangle class in the 9-rectangle module."""


class Square(__import__("9-rectangle").Rectangle):
    """Initialize the size of the square and validate it as an integer"""
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """Return the square of the size of the square"""
        return self.__size * self.__size

    def __str__(self):
        """Return a string representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
