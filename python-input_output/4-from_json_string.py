#!/usr/bin/python3
"""
Contain json function
"""
from json import loads


def from_json_string(my_str):
    """
    Transform string to json
    """
    return loads(my_str)
