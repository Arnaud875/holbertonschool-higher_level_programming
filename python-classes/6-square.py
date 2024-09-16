#!/usr/bin/python3
"""
Square class with constructor (size attribut)
"""


class Square:
    """
    Square class
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Square class constructor with size,position private attribut
        """
        self.__size = size
        self.__position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive")

        if not all(isinstance(v, int) for v in value):
            raise TypeError("position must be a tuple of 2 positive")

        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive")

        self.__position = value

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
        Print a square with size and position
        """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
