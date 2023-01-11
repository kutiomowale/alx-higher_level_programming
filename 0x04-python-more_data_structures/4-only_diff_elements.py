#!/usr/bin/python3

"""Only differents

A module that defines a function, that returns a set of all elements
present in only one set.
"""


def only_diff_elements(set_1, set_2):
    """Only differents

    A function that returns a set of all elements present in only one set.

    Args:
        set_1 (set): The first set
        set_2 (set): The second set

    Returns:
        The set of elements present in either sets but not both
    """
    # elements in set_1 or set_2 but not both
    return set_1 ^ set_2
