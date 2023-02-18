#!/usr/bin/python3
"""Write to a file
Function definition for write_file"""


def write_file(filename="", text=""):
    """Write to a file

    A function that writes a string to a text file (UTF8)
    and returns the number of characters written
    File permission exceptions are not managed
    The file is created if doesn’t exist.
    Contents of the file are overwritten if it already exists.

    Args:
        filename (str): Name of text file
        text (str): The string

    Returns:
        The number of characters written

    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
