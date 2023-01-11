#!/usr/bin/python3

"""Multiply by using map

A module that defines a function,
that returns a list with all values multiplied by a number
without using any loops.

Returns a new list:
Same length as my_list
Each value should be multiplied by number
Initial list should not be modified
You are not allowed to import any module
You have to use map
Your file should be max 3 lines

"""


def multiply_list_map(my_list=[], number=0):
    """Multiply by using map

    A function that returns a list with all values multiplied by a number
    without using any loops
    Returns a new list:                  Same length as my_list
    Each value should be multiplied by number
    Initial list should not be modified
    You are not allowed to import any module
    You have to use map
    Your file should be max 3 lines

    Args:
        my_list (list): The list
        number (int): The number

    Returns:
        A new list
    """
    return list(map((lambda x: x * number), my_list))
