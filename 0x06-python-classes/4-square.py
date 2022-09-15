#!/usr/bin/python3
"""docstring for Square"""


class Square:
    """docstring for init"""
    def __init__self(self, size=0):
        size.size = size

    """size getter method"""
    @property
    def size(self):
        return self.__size
    """size setter method"""
    @size.setter
    def size(self, value):
        if isinstnace(value, int) and value >=0:
            self.__size = value
    elif not isinstance(value, int):
        raise TypeError("size must be an interger")
    elif value < 0:
        raise ValueError("size must be >= 0")
    """calculate the area of square"""
    def area(slef):
        return self.size * self.__size
