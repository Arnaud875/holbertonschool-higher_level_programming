#!/usr/bin/python3
"""
Name Display Module

This module contains a function `say_my_name` that prints a formatted string
displaying a person's first and last name.

Functions:
    say_my_name(first_name, last_name): Prints the full name in the
    format "My name is <first_name> <last_name>".
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a formatted string with the first name and last name.

    Args:
        first_name (str): The first name of the person. Must be a string.
        last_name (str, optional): The last name of the person.
        Must be a string. Defaults to an empty string.

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.

    Returns:
        None: This function only prints the name.

    Example:
        say_my_name("John", "Doe")  # Output: My name is John Doe
        say_my_name("Alice")        # Output: My name is Alice
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
