#!/usr/bin/python3
class Square(__import__("9-rectangle").Rectangle):
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        return self.__size * self.__size
