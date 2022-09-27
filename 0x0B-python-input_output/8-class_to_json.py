#!/usr/bin/python3

"""
contains the "class_to json" function 
"""


def class_to_json(obj):
    """returrns the dictionarty description with simple data structure 
    (list, dictionary, sting, interger and boolean)
    for JSON serialization of an object
    """
    return obj.__dict__
