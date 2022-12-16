#!/usr/bin/pyhon3
"""afuction that finds a peak in
    alist of unsorted intergers
"""


def find_peak(list_of_integers):
    """function that finds peak in a list"""
    if list_of_integers == []:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
