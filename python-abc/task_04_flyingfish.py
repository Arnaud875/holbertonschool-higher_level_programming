#!/usr/bin/python3
"""
Contains classes
"""
from abc import ABC, abstractmethod


class Fish(ABC):
    """
    Fish class
    """
    @abstractmethod
    def swim(self):
        print("The fish is swimming")

    @abstractmethod
    def habitat(self):
        print("The fish lives in water")


class Bird(ABC):
    """
    Bird class
    """
    @abstractmethod
    def fly(self):
        print("The bird is flying")

    @abstractmethod
    def habitat(self):
        print("The fish lives in water")


class FlyingFish(Fish, Bird):
    """
    FlyingFish class
    """
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
