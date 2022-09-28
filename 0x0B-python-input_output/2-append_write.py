#!/usr/bin/python3
"""
Contains the fucntion "append_write"
"""


def append_write(filename="", text=""):
    """returns the number of chars appended to the "filename" from "text" """
    with open(filename, 'a', encoding= 'utf=8') as f:
        for char in text:
            f.write(char)
        return len(text)
