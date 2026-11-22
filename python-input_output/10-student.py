#!/usr/bin/python3
"""Module that defines a class Student."""


class Student:
    """A student with a first name, last name and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary description of a Student instance.

        If attrs is a list of strings, only those attributes are retrieved.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
