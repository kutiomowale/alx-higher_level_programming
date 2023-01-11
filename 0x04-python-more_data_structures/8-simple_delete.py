#!/usr/bin/python3

"""Simple delete by key

A module that defines a function,
that deletes a key in a dictionary.
"""


def simple_delete(a_dictionary, key=""):
    """Simple delete by key

    A function that deletes a key in a dictionary.
    Key argument will be always a string
    If a key doesn’t exist, the dictionary wont't change

    Args:
        a_dictionary (dictionary): The dictionary
        key (str): The key

    Returns:
        The updated dictionary
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
