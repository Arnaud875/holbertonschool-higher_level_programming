#!/usr/bin/python3
"""
Contain json function
"""
from sys import argv


if __name__ == "__main__":
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = \
        __import__("6-load_from_json_file").load_from_json_file

    data = []

    try:
        data = load_from_json_file("add_item.json")
    except Exception as e:
        pass

    data.extend(argv[1:])
    save_to_json_file(data, "add_item.json")
