#!/usr/bin/env python3
"""
Module that defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    Base class for geometric shapes.
    Provides common validation and interface methods.
    """


    def area(self):
        """
        Raises an exception because area is not implemented.

        Raises:
            Exception: area is not implemented
        """
        raise Exception("[{}]area is not implemented".format(self.__class__.__name__))

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Args:
            name (str): The name of the value
            value (int): The value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """
        if isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
