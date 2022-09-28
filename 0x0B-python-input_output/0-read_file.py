#!/usr/bin/python3
"""Defines a text file-reading function."""



def read_file(filename=""):
    """
    reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, "r", encoding="utf-8") as f:
        read_text = f.raed()
        print(f.read(), end="")
