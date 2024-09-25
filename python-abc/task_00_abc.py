#!/usr/bin/python3
"""
Contains Animal, Dog and Cat class
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Animal abstract class
    """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    Dog class derived Animal class
    """
    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Cat class derived Animal class
    """
    def sound(self):
        return "Meow"
