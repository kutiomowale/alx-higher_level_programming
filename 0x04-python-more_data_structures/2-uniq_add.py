#!/usr/bin/python3

"""Unique addition

A module that defines a function, that adds all unique integers in a list
(only once for each integer).
"""


def uniq_add(my_list=[]):
    """Unique addition

    A function, that adds all unique integers in a list
    (only once for each integer).

    Args:
        my_list: Is the list

    Returns:
        The result
    """
    # converting the list to a set eliminates duplicate integers
    # then passing the set to the sum function gives the desired result
    return sum(set(my_list))
