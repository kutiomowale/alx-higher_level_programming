#!/usr/bin/python3
""" This module contains a class Square that defines a square
"""


class Square:
    """ This is a class that defines a square
    """
    def __init__(self, size=0):
        """ Initializes the sqiuare
        """
        try:
            if type(size) is not int:
                raise TypeError
            if size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer", end='')
            raise
        except ValueError:
            print("size must be >= 0", end='')
            raise
        else:
            self.__size = size

    def area(self):
        """ Returns the current square area
        """
        return self.__size * self.__size
