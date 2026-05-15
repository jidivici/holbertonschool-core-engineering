#!/usr/bin/env python3
"""Module that defines the square class that inherits from Rectangle."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square, inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a new Square."""
        self.integer_validator("size", size)
        self.size = size
        super().__init__(size, size)

    def __str__(self):
        """Return string representation of Square."""
        return "[Square] {}".format(str(super())[11:])
