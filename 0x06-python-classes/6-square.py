#!/usr/bin/python3
""" This module contains a class Square that defines a square
"""


class Square:
    """ This is a class that defines a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Initializes the square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ returns the size of the square
            value is the size to be set
        """
        return self.__size

    @size.setter
    def size(self, value):
        try:
            if type(value) != int:
                raise TypeError
            if value < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer", end='')
            raise
        except ValueError:
            print("size must be >= 0", end='')
            raise
        else:
            self.__size = value

    @property
    def position(self):
        """ returns the position of the square
            value is the position to be set
        """
        return self.__position

    @position.setter
    def position(self, value):
        try:
            if type(value) != tuple:
                raise TypeError
            if len(value) != 2:
                raise TypeError
            if value[0] < 0 or value[1] < 0:
                raise TypeError
        except TypeError:
            print("position must be a tuple of 2 positive integers", end='')
            raise
        else:
            self.__position = value

    def area(self):
        """ Returns the current square area
        """
        return self.__size * self.__size

    def my_print(self):
        """ prints in stdout the square with the character #
            if size is equal to 0, it prints an empty line
            for position[0] > 0, spaces are used
            for position[1] > 0, newlines are used
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
