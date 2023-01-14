#!/usr/bin/python3
"""This module is for the add_integer funtion

The function takes one or two arguments and return the sum
The second argument is set to 98 by degault
Only integers or floats are allowed
Floats are converted to integers

"""


def add_integer(a, b=98):
    """A function that adds 2 integers

    Args:
        a : First integer
        b : Second integer(98 default)

    Returns:
        The sum of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
