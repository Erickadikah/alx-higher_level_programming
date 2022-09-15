#!/usr/bin/python3
"""docstring for Square"""


class Square:
    """docstring for init"""
    def __init__(self, size=0):
        if isinstance(size, int) and size >= 0:
            self.__size = size
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return (self.__size ** 2)
