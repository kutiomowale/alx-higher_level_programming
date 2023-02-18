#!/usr/bin/python3
"""Class to JSON
Function definition for class_to_json
"""


def class_to_json(obj):
    """Class to JSON

    A function that returns the dictionary description
    with simple data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object:
    All attributes of the obj Class are serializable:
    list, dictionary, string, integer and boolean

    Args:
        obj: is an instance of a Class

    Returns:
        The dictionary description of the object

    """
    return obj.__dict__
