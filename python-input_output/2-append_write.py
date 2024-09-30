#!/usr/bin/python3
"""
Contains append function
"""


def append_write(filename="", text=""):
    """
    Append text into filename file arg
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
