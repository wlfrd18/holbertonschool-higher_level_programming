#!/usr/bin/python3
"""
    module that cretaes a function
"""


def inherits_from(obj, a_class):
    """Function that validate or no if an object inherits

    Arguments:
        obj -> object to compare
        a_class -> class to be compare

    Returns:
        True or false
    """
    return isinstance(obj, a_class) and not type(obj) = a_class
