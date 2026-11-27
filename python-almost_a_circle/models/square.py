#!/usr/bin/python3
"""Defines the Square class with update method."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the Square (width then height)."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Assign arguments to attributes via *args or **kwargs."""
        attrs = ["id", "size", "x", "y"]
        if args and len(args) > 0:
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)
