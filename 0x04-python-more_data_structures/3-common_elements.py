#!/usr/bin/python3

"""Present in both

A module that defines a function, that returns a set of common elements
in two sets.
"""


def common_elements(set_1, set_2):
    """Present in both

    A function that returns a set of common elements in two sets.

    Args:
        set_1 (set): The first set
        set_2 (set): The second set

    Returns:
        The set of common elements
    """
    # elements in both sets
    return set_1 & set_2
