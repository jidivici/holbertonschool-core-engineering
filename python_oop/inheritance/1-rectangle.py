#!/usr/bin/env python3
"""Module that defines the Rectangle class that inherits from BaseGeometry."""

BaseGeometry = __import__('0-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a rectangle, inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new Rectangle."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
