#!/usr/bin/python3
"""Module that defines a function to append a string to a text file."""


def append_write(filename="", text=""):
    """Appends a string to a UTF8 file, returns the characters added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
