#!/usr/bin/python3
"""3-say_my_name module.

This module provides the function say_my_name(first_name, last_name="")
that prints a name.
"""


def say_my_name(first_name, last_name=""):
    """Print My name is <first name> <last name>.

    Args:
        first_name: string, the first name.
        last_name: string, the last name (default is empty).

    Raises:
        TypeError: if first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
