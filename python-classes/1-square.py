#!/usr/bin/python3
"""Module that defines a Square class with a private size."""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: the size of the square (no validation yet).
        """
        self.__size = size
