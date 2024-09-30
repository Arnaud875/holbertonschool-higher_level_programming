#!/usr/bin/python3
"""
Contain serialize and deserialize functions
"""
from pickle import load, dump


def serialize_and_save_to_file(data, filename):
    """
    Serialize json data
    """
    with open(filename, "wb") as f:
        dump(data, f)


def load_and_deserialize(filename):
    """
    Deserialize json data
    """
    with open(filename, "rb") as f:
        return load(f)
