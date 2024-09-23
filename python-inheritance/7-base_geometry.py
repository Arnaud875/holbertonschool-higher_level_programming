#!/usr/bin/python3
class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
