#!/usr/bin/python3
""" This module contains a class Square that defines a square
"""


class Square:
    """ This is a class that defines a square
    """
    def __init__(self, size=0):
        """ Initializes the sqiuare
        """
        self.__size = size

    @property
    def size(self):
        """ returns the size of the square
            value is the size to be set
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Returns the current square area
        """
        return self.__size * self.__size
