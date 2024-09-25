#!/usr/bin/python3
"""
Contains CountedIterator class
"""


class CountedIterator:
    """
    CountedIterator class
    """
    def __init__(self, data):
        self.__data = iter(data)
        self.__count = 0

    def __next__(self):
        self.__count += 1
        return next(self.__data)

    def get_count(self):
        return self.__count
