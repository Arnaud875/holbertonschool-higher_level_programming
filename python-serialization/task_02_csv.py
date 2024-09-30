#!/usr/bin/python3
"""
Contain csv function
"""
import json
import csv


def convert_csv_to_json(filename=""):
    """
    Convert csv data to json format
    """
    data = list(csv.DictReader(open(filename, "r")))

    with open("data.json", "w") as f:
        json.dump(data, f)
