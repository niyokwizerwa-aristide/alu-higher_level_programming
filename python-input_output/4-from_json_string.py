#!/usr/bin/python3
"""Module that defines a function to build an object from a JSON string."""
import json


def from_json_string(my_str):
    """Returns the Python object represented by a JSON string."""
    return json.loads(my_str)
