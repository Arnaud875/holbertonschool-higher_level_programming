#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    length = len(tuple_b) - 1
    new_tuple = []

    for i in range(len(tuple_a) - 1):
        res = tuple_a[i]
        if i + 1 <= length:
            res += + tuple_b[i]
        new_tuple.append(res)

    return tuple(new_tuple)
