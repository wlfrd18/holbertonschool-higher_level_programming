#!/usr/bin/python3


"""
This module creates a new class Square
"""


class Square:
    """ init method class """
    def __init__(self, size=0):
        if (type(size) is not int):
            raise ValueError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """ Return the area of square """
        return (self.__size * self.__size)
