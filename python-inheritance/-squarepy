#!/usr/bin/python3
"""
    Module that creates a Square class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class

    Arguments:
        Rectangle -> Parent class
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))
