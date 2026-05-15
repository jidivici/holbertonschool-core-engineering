#!/usr/bin/env python3
"""Module that defines the square class that inherits from Rectangle."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square, inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a new Square."""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Calculate the area of the square."""
        print("{}".format(self.width * self.height))

    def __str__(self):
        """Return the string representation of the square."""
        print("[Square] {}/{}".format(self.width, self.height))
