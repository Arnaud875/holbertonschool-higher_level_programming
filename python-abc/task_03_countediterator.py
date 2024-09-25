#!/usr/bin/python3
"""
Contains CountedIterator class
"""


class CountedIterator:
    """
    CountedIterator class
    """
    def __init__(self, data):
        self.iterator = iter(data)
        self.__count = 0

    def __next__(self):
        self.__count += 1
        return next(self.iterator)

    def get_count(self):
        return self.__count

data = [1, 2, 3, 4]
counted_iter = CountedIterator(data)

try:
    while True:
        item = next(counted_iter)
        print(f"Got {item}, total {counted_iter.get_count()} items iterated.")
except StopIteration:
    print("No more items.")