#!/usr/bin/python3
"""Read file
Function definition for read_file"""


def read_file(filename=""):
    """Read file

    A function that reads a text file (UTF8) and prints it to stdout

    File permission or file doesn't exist exceptions are not managed

    Args:
        filename (str): Name of text file

"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
