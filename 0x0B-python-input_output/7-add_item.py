#!/usr/bin/python3

"""module 7-save_to_json_file.
    writes an object to text file,
    using a json representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """writes the representation of my_obj
    to filename.
    Args:
        - my_obj: object to write 
        - filename: file to write into
    """

    with open(filename, 'w+') as f:
        json.dump(my_obj, f)
