#!/usr/bin/python3
"""
Contain json function
"""
from json import dump


def save_to_json_file(my_obj, filename):
    """
    Save json data to file
    """
    with open(filename, "w") as f:
        dump(my_obj, f)
