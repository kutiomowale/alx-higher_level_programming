#!/usr/bin/python3

"""Best score

A module that defines a function,
that returns a key with the biggest integer value
"""


def best_score(a_dictionary):
    """Best score

    A function that returns a key with the biggest integer value
    You can assume that all values are only integers
    If no score found, return None
    You can assume all students have a different score
    Args:
        a_dictionary (dictionary): The dictionary

    Returns:
        The key with the biggest value, or None if no score is found
    """
    if not a_dictionary:
        return None
    # create a new dictionary with values and keys swapped
    new_dictionary = {a_dictionary[i]: i for i in a_dictionary}
    # find the biggest key in new_dictionary
    value = max(new_dictionary)
    # use this to get the required key
    return new_dictionary[value]
