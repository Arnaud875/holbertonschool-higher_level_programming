#!/usr/bin/python3
"""
Module: text_formatter
This module provides a function to format and print text with specified
punctuation rules.
"""


def text_indentation(text):
    """
    Prints a string with two new lines after each '.', '?', or ':'.
    Args:
        text (str): The input string to be formatted and printed.
    Raises:
        TypeError: If the input `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    skip_space = True
    for char in text:
        if skip_space and char == " ":
            continue
        print(char, end="")

        if char in ".?:":
            print("\n")
            skip_space = True
        else:
            skip_space = False
