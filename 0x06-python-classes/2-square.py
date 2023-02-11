#!/usr/bin/python3
""" This module contains a class Square that defines a square
"""


class Square:
    """ This is a class that defines a square
    """
    def __init__(self, size=0):
        """ Initializes the sqiuare
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
