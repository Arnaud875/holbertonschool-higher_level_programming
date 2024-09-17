#!/usr/bin/python3
"""
Rectange class
"""


class Rectangle:
    """
    Rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Rectangle constructor to initialize width and heigth
        private attributs
        """
        self.__height = height
        self.__width = width

        Rectangle.number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        a = rect_1.area()
        b = rect_2.area()

        if a == b:
            return rect_1
        return rect_1 if a > b else rect_2

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
                result += "{}".format(self.print_symbol)

            if i+1 < self.__height:
                result += "\n"
        return result

    def __repr__(self):
        """
        Return a string representation of the rectangle class
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Rectange delete constructor
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
