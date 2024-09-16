#!/usr/bin/python3
"""
Module that defines the Square class with size and position attributes,
along with methods to compute the area and print the square.
"""


class Square:
    """
    A class that represents a square.
    Attributes:
        size (int): The size of one side of the square.
        position (tuple): The (x, y) coordinates indicating
        the starting position for printing the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with an optional size and position.
        Args:
            size (int): The size of the square (must be >= 0). Default is 0.
            position (tuple): A tuple of 2 positive integers (x, y)
            representing the starting position. Default is (0, 0).
        """
        self.size = size  # Calls the size setter to validate
        self.position = position  # Calls the position setter to validate

    @property
    def position(self):
        """
        Retrieves the position of the square.
        Returns:
            tuple: The current position as a tuple (x, y).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.
        Args:
            value (tuple): A tuple of 2 positive integers
            representing the new position.
        Raises:
            TypeError: If value is not a tuple or does
            not contain exactly 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not all(isinstance(v, int) for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    @property
    def size(self):
        """
        Retrieves the size of the square.
        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        Args:
            value (int): The new size of the square (must be >= 0).
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Computes the area of the square.
        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square using the '#' character,
        taking into account the size and position.
        If the size is 0, it prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        # Print vertical offset (new lines for position[1])
        for _ in range(self.__position[1]):
            print("")

        # Print the square with horizontal offset
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
