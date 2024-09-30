#!/usr/bin/python3
"""
Contains json function
"""
from json import dumps


def to_json_string(my_obj):
    """
    Transorm json to string
    """
    return dumps(my_obj)
