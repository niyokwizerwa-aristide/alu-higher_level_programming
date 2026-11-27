#!/usr/bin/python3
"""4-print_square module.

This module provides the function print_square(size)
that prints a square with the character #.
"""


def print_square(size):
    """Print a square of the character # with side length size.

    Args:
        size: integer, the length of the side of the square.

    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
