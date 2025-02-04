#!/usr/bin/python3
"""
    Module that creates a BaseGeometry class
"""


class BaseGeometry:
    """
    Class BaseGeometry
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function that validates a value

        Arguments:
            name  -- Name
            value (int) -- Value to be validate

        Raises:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
