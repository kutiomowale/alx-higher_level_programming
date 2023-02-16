#!/usr/bin/python3
"""Function defintion for add_attribute"""


def add_attribute(obj, new_attr_name, attr):
    """A function that adds a new attribute to an object if it’s possible

    Args:
        obj: The object
        new_attr_name: The name of the new attribute
        attr: The new attribute

    Raises:
        TypeError: If the object can’t have new attribute

    """
    if hasattr(obj, "__dict__"):
        obj.__dict__[new_attr_name] = attr
    else:
        raise TypeError("can't add new attribute")
