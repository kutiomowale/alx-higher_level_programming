#!/usr/bin/python3
"""Append to a file
Function definition for append_file"""


def append_write(filename="", text=""):
    """Append to a file

    A function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added.
    File permission or file doesn't exceptions are not managed
    The file is created if doesn’t exist.

    Args:
        filename (str): Name of text file
        text (str): The string

    Returns:
        The number of characters added

"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
