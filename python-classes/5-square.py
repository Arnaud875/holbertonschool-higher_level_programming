#!/usr/bin/python3
"""
Square class with constructor (size attribut)
"""


class Square:
    """
    Square class
    """
    def __init__(self, size=0):
        """
        Square class constructor with size private attribut
        """
        self.__size = size

    @property
    def size(self):
        """
        Get size private attribut
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set size private attribut
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Return the square area
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print a square with size (__size)
        """
        if self.__size == 0:
            print("")
            return

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
