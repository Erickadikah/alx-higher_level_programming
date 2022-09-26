#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.

    Args:
        obj (any object): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        if obj is an instance or inherited instance of a class - True.
        other wise - False.
    """
    if isinstance(object, a_class):
        return True
    return False
