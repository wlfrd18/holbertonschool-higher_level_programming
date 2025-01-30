#!/usr/bin/python3
""" This module creates a new class Square
"""


class Rectangle:
    """ Rectangle class
    """

    def __init__(self, width=0, height=0):
        """Init method

        Keyword Arguments:
            width [int] -- widht of triangle default: 0
            height [int] -- height of triangle default: 0
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """Property to height of triangle

        Returns:
        int --  Private height attribute of triangle
        """
        return self.__height

    @property
    def width(self):
        """Property to width of triangle

        Returns:
            Int -- Private width attribute of triangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Function that set the width of triangle

        Arguments:
            value [int] -- Widht value to be set to triangle

        Raises:
            TypeError: width must be an integer
            ValueError: width must be greater or eaual to 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Function that set the height of triangle

        Arguments:
            value [int] -- Height value to be set to triangle

        Raises:
            TypeError: height must be an integer
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Function to calculate the area of a rectangle

        Returns:
            int -- the area of rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """Function to calculate the perimeter of a rectangle

        Returns:
            int -- the perimeter of rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2*(self.__height + self.__width)

    def __str__(self):
        """Function that prints a rectangle

        Returns:
            String -- The printed rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            string = ""
            for _ in range(self.__height):
                string += "#" * self.__width
                if _ < self.__height - 1:
                    string += "\n"
        return string

    def __repr__(self):
        """Function repr of rectangle

        Returns:
            String -- String to representate a object
        """
        return "Rectangle(" + str(self.__width)+", "+str(self.__height) + ")"

    def __del__(self):
        """Function that deletes an instance of rectangle
        """
        print("Bye rectangle...")
