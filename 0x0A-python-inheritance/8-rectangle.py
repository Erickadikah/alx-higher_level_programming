#!/usr/bin/python3

"""class Rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry.py').BaseGeaometry



class Rectangle(BaseGeometry):
    """A representattion of a rectangle"""
    def __init__(self, width, height):
        """instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.interger_validator("height", height)
        self.__height = height
