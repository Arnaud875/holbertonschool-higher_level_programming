#!/usr/bin/python3
"""
Rectange class
"""


class Rectangle:
    """
    Rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        Rectangle constructor to initialize width and heigth
        private attributs
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        Get width private attribut
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set width private attribut
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Get height private attribut
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set height private attribut
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Return the size of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Return the perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Return the rectangle into string
        """
        if self.__height == 0 or self.__width == 0:
            return ""

        result = ""
        for i in range(self.__height):
            for j in range(self.__width):
                result += "#"

            if i+1 < self.__height:
                result += "\n"
        return result
