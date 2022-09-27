#!/usr/bin/python3
"""module: 1-my_list
"""


class Mylist(list):
    """Represents a mylist
    """


    def print_sorted(self):
        """
        prints the list, but sorted
        """
        print(sorted(self))
