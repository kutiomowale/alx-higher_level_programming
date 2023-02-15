#!/usr/bin/python3
"""inherits_from function definition"""


def inherits_from(obj, a_class):
    """A function that checks if an object
    is an instance of a class that inherited (directly or indirectly) out of
    a given class

    Args:
        obj: The object
        a_class: The class

    Reurns:
        True if it is, False otherwise

    """
    return isinstance(obj, a_class) and type(obj) is not a_class
