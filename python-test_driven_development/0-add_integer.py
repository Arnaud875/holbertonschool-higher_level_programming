#!/usr/bin/python3
"""
Defining a function for adding numbers
Functions:
    add_integer(a, b=98): Return the addication of a and b.
"""


def add_integer(a, b=98):
    """Adds two numbers and returns their sum. If either
of the inputs is a float, it is cast to an integer before addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
