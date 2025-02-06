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
        if isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
