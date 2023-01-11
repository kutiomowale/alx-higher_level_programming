#!/usr/bin/python3

"""Update dictionary

A module that defines a function,
that replaces or adds key/value in a dictionary.
"""


def update_dictionary(a_dictionary, key, value):
    """Update dictionary

    A function that replaces or adds key/value in a dictionary.
    Key argument will be always a string
    Value argument will be any type
    If a key exists in the dictionary, the value will be replaced
    If a key doesn’t exist in the dictionary, it will be created

    Args:
        a_dictionary (dictionary): The dictionary
        key (str): The key
        value: The value
    Returns:
        The updated dictionary
    """
    a_dictionary[key] = value
    return a_dictionary
