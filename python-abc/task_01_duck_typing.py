#!/usr/bin/python3
"""
Contains multiple classes
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Shape class
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    Circle class
    """
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """
    Rectangle class
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        return 2 * (self.__height + self.__width)


def shape_info(arg):
    """
    shape_info function
    """
    print("Area: {}".format(arg.area()))
    print("Perimeter: {}".format(arg.perimeter()))
