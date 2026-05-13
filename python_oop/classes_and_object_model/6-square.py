#!/usr/bin/env python3
"""Module that defines a Square class."""


class Square:
    """Defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get or set the size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Compute the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character '#'."""
        print(str(self))

    def __str__(self):
        """Return a string representation of the square.

        Returns:
            str: The square as a string of '#' characters.
        """
        if self.size == 0:
            return ""
        vertical_spaces = "\n" * self.position[1]
        result = vertical_spaces
        for i in range(self.size):
            result += " " * self.position[0] + "#" * self.size
            if i < self.size - 1:
                result += "\n"
        return result

    @property
    def position(self):
        """Get or set the position of the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        return self.__position

    @position.setter
    def position(self, position):
        if (not isinstance(position, tuple)
                or len(position) != 2
                or not isinstance(position[0], int)
                or not isinstance(position[1], int)
                or position[0] < 0
                or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = position
