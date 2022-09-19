#!/usr/bin/python3
"""module 1-rectangle
defines a rectangle class.
"""



class Rectangle:
        """rectangle class defined by width and height"""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle isisntace"""

        self.width = width
        self.height = height


    @property
    def width(self):
        """Retreves the width of a Rectangle instance."""
        return self.__width

   @width.setter
    def width(self, value):
        """sets the width of a rectangle is instance"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retreives the height of a rectangle instances."""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of a rectangle instance"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
