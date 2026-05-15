#!/usr/bin/env python3
"""Module that defines the square class that inherits from Rectangle."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square, inherits from Rectangle."""

    def __init__(self, width, height):
        """Initialize a new Square."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
