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
        Square class constructor with size private attribut
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size <= 0:
            raise TypeError("size must be >= 0")

        self.__size = size
        self.__position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive ")

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
            raise TypeError("size must be >= 0")
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

        if self.__position[1] > 0:
            print("".join(["\n" for i in range(self.__position[1])]), end="")

        for i in range(self.__size):
            print("".join([" " for i in range(self.__position[0])]), end="")
            for j in range(self.__size):
                print("#", end="")
            print("")
