#!/usr/bin/python3
"""
module that creates a function
"""


def is_same_class(obj, a_class):
    """Function that validate if a obj belong to a class

    Arguments:
        obj - Object to be compared
        a_class - Class to compare

    Returns:
        False or true
    """
    return type(obj) == a_class

