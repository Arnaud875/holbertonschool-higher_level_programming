#!/usr/bin/python3
"""
Contains classes
"""
from abc import ABC, abstractmethod


class SwimMixin(ABC):
    """
    SwimMixin class
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin(ABC):
    """
    FlyMixin class
    """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class
    """
    def roar(self):
        print("The dragon roars!")
