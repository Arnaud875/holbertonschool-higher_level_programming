#!/usr/bin/python3
"""
Contain json function
"""


def class_to_json(obj):
    """
    Return the description of object
    """
    return obj.__dict__
