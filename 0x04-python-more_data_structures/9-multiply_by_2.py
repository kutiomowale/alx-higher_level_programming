#!/usr/bin/python3

"""Multiply by 2

A module that defines a function,
that returns a new dictionary with all values multiplied by 2
"""


def multiply_by_2(a_dictionary):
    """Multiply by 2

    A function that returns a new dictionary with all values multiplied by 2
    You can assume that all values are only integers
    Returns a new dictionary
    Args:
        a_dictionary (dictionary): The dictionary

    Returns:
        The new dictionary
    """
    return {i: a_dictionary[i] * 2 for i in a_dictionary}
