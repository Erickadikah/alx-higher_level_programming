#!/usr/bin/python3
"""this function returns the JSON representation of an object"""

import json

def to_json_string(my_obj):
    """returns the json representation of an object (string)"""
    return json.dumps(my_obj)
