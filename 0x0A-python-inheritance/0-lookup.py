#!/usr/bin/python3
"""lookup function definition"""


def lookup(obj):
    """A function that returns

    the list of available attributes and methods of an object

    Args:
        obj : The object

    Returns:the list of available attributes and methods of obj
    """
    return dir(obj)
