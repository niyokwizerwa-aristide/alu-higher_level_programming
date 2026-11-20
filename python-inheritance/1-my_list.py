#!/usr/bin/python3
"""Module that defines a class MyList that inherits from list."""


class MyList(list):
    """Class that inherits from list and can print itself sorted."""

    def print_sorted(self):
        """Prints the list in ascending order without modifying it."""
        print(sorted(self))
