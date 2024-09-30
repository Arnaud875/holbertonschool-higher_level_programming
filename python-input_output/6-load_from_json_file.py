#!/usr/bin/python3
"""
Contain json function
"""
from json import load


def load_from_json_file(filename):
    """
    Load json data from file
    """
    with open(filename, "r") as f:
        return load(f)
