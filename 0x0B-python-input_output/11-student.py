#!/usr/bin/python3
""" Student to JSON """


class Student:
    """ New class student """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance """
        if (type(attrs) == list and all(types(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):

        for k, v in json.items():
            setattr(self, k, v)
