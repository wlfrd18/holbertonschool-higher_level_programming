#!/usr/bin/python3


"""
This module creates a new class Square
"""


class Square:
    """ __init__ method class """
    def __init__(self, size=0):
            self.__size = size

    def area(self):
        """ Return the area of square """
        return (self.__size * self.__size)

    @property
    def size(self):
        """ Return size of square """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size of square """
        if (type(value) != int):
            raise ValueError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
