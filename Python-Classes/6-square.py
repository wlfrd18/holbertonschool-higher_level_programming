#!/usr/bin/python3


"""
This module creates a new class Square
"""


class Square:
    """ __init__ method class """
    def __init__(self, size=0, position=(0, 0)):
            self.__size = size
            self.position = position

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

    def my_print(self):
        """ Print a square """

        pos = self.__position
        siz = self.__size
        if self.__size is 0:
            print("")
        else:
            for _ in range(pos[1]):
                print("")
            for _ in range(siz):
                for j in range(siz + pos[0]):
                    if j < pos[0]:
                        print(" ", end='')
                    else:
                        print("#", end='')
                print("")

    @property
    def position(self):
        """ Return position """

        return self.__position

    @position.setter
    def position(self, value):
        """Set value """

        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
