#!/usr/bin/python3
"""is_same_class function definition"""


def is_same_class(obj, a_class):
    """A function that checks if an object
    is exactly an instance of a given class

    Args:
        obj: The object
        a_class: The class

    Reurns:
        True if it is, False otherwise

    """
    return type(obj) is a_class
