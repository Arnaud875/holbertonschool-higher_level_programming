#!/usr/bin/python3
"""
Rectangle class representing a rectangle shape.
"""


class Rectangle:
    """
    Represents a rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): Width of the rectangle (default 0).
            height (int): Height of the rectangle (default 0).
        """
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Gets the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The new width.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The new height.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle, or 0 if any side is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Returns a string representation
        of the rectangle using the print_symbol.

        Returns:
            str: String representation of the rectangle, or empty string if
            either width or height is 0.
        """
        if self.__height == 0 or self.__width == 0:
            return ""

        result = ""
        for i in range(self.__height):
            result += "{}".format(self.print_symbol) * self.__width
            if i + 1 < self.__height:
                result += "\n"
        return result

    def __repr__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: String that can recreate the rectangle instance.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Called when the rectangle instance is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
