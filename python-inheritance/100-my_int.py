#!/usr/bin/python3
"""Module that defines a class MyInt that inherits from int."""


class MyInt(int):
    """A rebel integer with inverted == and != operators."""

    def __eq__(self, other):
        """Returns True when the values are different (inverted ==)."""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Returns True when the values are equal (inverted !=)."""
        return int.__eq__(self, other)
