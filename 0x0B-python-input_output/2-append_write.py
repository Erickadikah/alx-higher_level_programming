#!/usr/bin/python3
"""
Contains the function "append_write"
"""


def append_write(filename="", text=""):
    with open(filename, "a", encoding="utf") as f:
        return f.write(text)
