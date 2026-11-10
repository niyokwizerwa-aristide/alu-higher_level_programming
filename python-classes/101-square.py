#!/usr/bin/python3
"""Module that defines a Square class that can be printed."""


class Square:
    """A class that defines a square by its size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): the size of the square.
            position (tuple): the position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Raises:
            TypeError: if value is not a tuple of 2 positive integers.
        """
        if (type(value) is not tuple or len(value) != 2 or
                type(value[0]) is not int or type(value[1]) is not int or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #, offset by position.

        If size is 0, print an empty line.
        """
        print(str(self))

    def __str__(self):
        """Return the square as a string, offset by position.

        If size is 0, return an empty string.
        """
        if self.__size == 0:
            return ""
        lines = [""] * self.__position[1]
        row = " " * self.__position[0] + "#" * self.__size
        lines += [row] * self.__size
        return "\n".join(lines)
