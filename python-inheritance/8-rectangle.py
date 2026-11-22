#!/usr/bin/python3
"""Module that defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle with a private width and height."""

    def __init__(self, width, height):
        """Initializes a rectangle after validating width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
