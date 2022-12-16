#!/usr/bin/pyhon3
"""afuction that finds a peak in unsorted list
"""


def find_peak(list_of_integers):
    """function that finds peak in a list"""
    if len(list_of_integers) == 0:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
