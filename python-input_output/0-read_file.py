#!/usr/bin/python3
"""
Module contains read fonction
"""


def read_file(filename=""):
    """
    Read file by filename arg
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
