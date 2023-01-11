#!/usr/bin/python3

"""Print sorted dictionary

A module that defines a function, that prints a dictionary by ordered keys
"""


def print_sorted_dictionary(a_dictionary):
    """Print sorted dictionary

    A function that prints a dictionary by ordered keys
    You can assume that all keys are strings.
    Keys should be sorted by alphabetic order

    Args:
        a_dictionary (dictionary): The dictionary
    """
    # sorted(a_dict) return a sorted list of a_dict keys
    list = sorted(a_dictionary)
    for i in list:
        print(f"{i}: {a_dictionary[i]}")
