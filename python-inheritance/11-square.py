#!/usr/bin/python3
"""Module that defines a class Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square with a private size."""

    def __init__(self, size):
        """Initializes a square after validating size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Returns the description [Square] <width>/<height>."""
        return "[Square] {}/{}".format(self.__size, self.__size)
