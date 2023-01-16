#!/usr/bin/python3

"""A function that prints a square with the character#"""


def print_square(size):
    """Print square

    A function that prints a square with the character #

    Args:
        size (int) : The length of the square

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)