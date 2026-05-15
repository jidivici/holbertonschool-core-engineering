#!/usr/bin/env python3
"""Module that defines the Rectangle class that inherits from BaseGeometry."""
from base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a rectangle, inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
