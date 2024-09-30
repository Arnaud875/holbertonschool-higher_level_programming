#!/usr/bin/python3
"""
Contains write file
"""


def write_file(filename="", text=""):
    """
    Write text in filename arg
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
