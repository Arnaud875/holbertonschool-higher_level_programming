#!/usr/bin/python3
"""
Module: square_printer
This module provides a function to print a square of '#' characters.
"""


def print_square(size):
    """
    Prints a square of a given size using '#' characters.

    Args:
        size (int): The size of the square. Must be a non-negative integer.

    Raises:
        TypeError: If size is not an integer or is a negative float.
        ValueError: If size is less than 0.
    """
    if isinstance(size, float) and int(size) == 0:
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise TypeError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
