#!/usr/bin/python3
"""
Contains VerboseList class
"""
from abc import ABC, abstractmethod


class VerboseList(list):
    """
    VerboseList class
    """
    def append(self, value):
        print("Added [{}] to the list.".format(value))
        super().append(value)

    def extend(self, value):
        print("Extended the list with [{}] items.".format(len(value)))
        super().extend(value)

    def remove(self, value):
        print("Removed [{}] from the list.".format(value))
        super().remove(value)

    def pop(self, index=-1):
        value = super().pop(index)
        print("Popped [{}] from the list.".format(value))
