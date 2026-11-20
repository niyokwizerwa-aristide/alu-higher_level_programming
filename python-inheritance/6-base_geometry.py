#!/usr/bin/python3
"""Module that defines a class BaseGeometry."""


class BaseGeometry:
    """A class BaseGeometry with an unimplemented area method."""

    def area(self):
        """Raises an Exception because area is not implemented."""
        raise Exception("area() is not implemented")
