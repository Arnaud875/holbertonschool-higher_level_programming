#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a list with bumble algo"""
        tried_list = self.copy()
        size = len(tried_list)

        swapped = True
        while swapped:
            swapped = False
            for i in range(size - 1):
                if tried_list[i] > tried_list[i + 1]:
                    tried_list[i], tried_list[i + 1] = \
                        tried_list[i + 1], tried_list[i]
                    swapped = True
        print(tried_list)
