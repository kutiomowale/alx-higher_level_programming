#!/usr/bin/python3
"""is_kind_of_class function definition"""


def is_kind_of_class(obj, a_class):
    """A function that checks if an object
    is an instance of,
    or is an instance of a class that inherited from a given class

    Args:
        obj: The object
        a_class: The class

    Reurns:
        True if it is, False otherwise

    """
    return isinstance(obj, a_class)
