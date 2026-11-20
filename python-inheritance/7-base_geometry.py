#!/usr/bin/python3
"""Module that defines a class BaseGeometry with an integer validator."""


class BaseGeometry:
    """A class BaseGeometry with area and integer validation."""

    def area(self):
        """Raises an Exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an integer greater than 0."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
