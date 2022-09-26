#!/usr/bin/python3

"""Contains class Geometry"""
class BaseGeometry:
    """ A class with pub;lic instance methods area and intergere_validator"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates tha value is an integere greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

