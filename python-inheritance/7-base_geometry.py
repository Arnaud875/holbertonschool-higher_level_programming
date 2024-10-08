#!/usr/bin/python3
"""
Defines a base geometry class BaseGeometry.
"""


class BaseGeometry:
    """Reprsent base geometry."""
    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer."""
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
