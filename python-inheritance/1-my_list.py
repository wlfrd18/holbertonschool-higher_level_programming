#!/usr/bin/python3


"""
This module creates a new MyList Class
"""


class MyList(list):
    """My List class

    Arguments:
        list --
    """
    def print_sorted(self):
        """
        Function that print a sorted list
        """
        print(sorted(self))
