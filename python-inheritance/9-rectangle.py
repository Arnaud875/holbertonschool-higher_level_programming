#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""


class Rectangle(__import__("7-base_geometry").BaseGeometry):
    """Represent a rectangle using BaseGeometry."""
    def __init__(self, width, height):
        """Intialize a new Rectangle."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        return "[Rectange] {}/{}".format(self.__width, self.__height)
