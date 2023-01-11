#!/usr/bin/python3

"""Delete by value

A module that defines a function,
that deletes keys with a specific value in a dictionary
"""


def complex_delete(a_dictionary, value):
    """Delete by value

    A function that deletes keys with a specific value in a dictionary.
    If the value doesn’t exist, the dictionary won’t change
    All keys having the searched value have to be deleted

    Args:
        a_dictionary (dict): The dictionary to modify
        value: The value to use

    Returns:
        The modified dictionary
    """
    my_list = [i for i in a_dictionary if a_dictionary[i] == value]
    for i in my_list:
        del a_dictionary[i]
    return a_dictionary
