#!/usr/bin/python3
"""
    Module that creates a BaseGeometry class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class

    Arguments:
        BaseGeometry -> Parent class
    """
    def __init__(self, width, height):
        """Init method

        Arguments:
            width -> width of rectangle (int)
            height -> height of rectangle (int)
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
