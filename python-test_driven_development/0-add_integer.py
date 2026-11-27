#!/usr/bin/python3
"""0-add_integer module.

This module provides the function add_integer(a, b)
that adds two integers.
"""


def add_integer(a, b=98):
    """Add two integers.
    Floats are cast to integers before the addition.
    """
    if not isinstance(a, (int, float)) or a != a:
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or b != b:
        raise TypeError("b must be an integer")
    if a in (float("inf"), float("-inf")):
        raise TypeError("a must be an integer")
    if b in (float("inf"), float("-inf")):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
