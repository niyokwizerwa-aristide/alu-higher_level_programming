#!/usr/bin/python3
"""5-text_indentation module.

This module provides the function text_indentation(text)
that prints a text with 2 new lines after each of these
characters: ., ? and :
"""


def text_indentation(text):
    """Print text with 2 new lines after each '.', '?' and ':'.

    Args:
        text: string to print.

    Raises:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip(" ")
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n", end="")
            print()
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
