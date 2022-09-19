#!/usr/bin/python
"""Module 1-rectangle
Defines a rectangle class. 
"""


class Rectangle:
    """Rectangle class defined by width and height."""

    def __init__(self, width=0, height=0):
        """initializes a Rectangle instance.
        Args:
        width: width of the rectangle
        height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of Rectangle isntance."""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of rectangle isntance
        Args:
        value: value of the width, must be positive interger
        """
        if not isinstance(value, int):
            raise TypeError("widt must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retreives the height of a rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of a Rectangle istance.
        Args:
        value: value of the height, must be positive interger
        """
        if not isinstance(value, int):
            raise ValueError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
