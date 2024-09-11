#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for idx, c in enumerate(my_string):
        if c not in ["c", "C"]:
            new_str += c
    return new_str
