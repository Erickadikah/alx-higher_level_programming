#!/usr/bin/python3

"""
contains the class BaseGeometry and subclass rectangle
"""

Rectangle = __import__('9-rectangle.py').Rectangle

class Spuare(Rectangle):
    """isntantation of a square"""
    def __init__(self, size):
        """instatiation of the square"""
        self.interger_validator("size", size)
        self.__size = size
        sepre().__init__(size, size)

    def area(self):
        """returns the area of the square"""
        return self.size__size ** 2
