#!/usr/bin/python3

"""Weighted average!

A module that defines a function,
that returns the weighted average of all integers tuple (<score>, <weight>)
"""


def weight_average(my_list=[]):
    """Weighted average!

    A function that returns the weighted average of
    all integers tuple (<score>, <weight>)

    Args:
        my_list (list): A list of (<score>, <weight>)

    Returns:
        The weighted average, or 0 if the list is empty
    """
    if len(my_list) == 0:
        return 0
    numerator = sum([i[0] * i[1] for i in my_list])
    denominator = sum([i[1] for i in my_list])
    weighted_average = numerator / denominator
    return weighted_average
