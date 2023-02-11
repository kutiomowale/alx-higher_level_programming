#!/usr/bin/python3

""" This module defines a class for a square """


class Square:
    """ This class defines a square """
    def __init__(self, size=0, position=(0, 0)):
        """ Initializes an instace of a Square """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Retrieves the size of the square
            value is the size to be set
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ Retrieves the position of the square
            value is the position to be set
        """
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Returns the current square area """
        return self.__size * self.__size

    def my_print(self):
        """ Prints in the stdout the square with the character # """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """ Returns a string representation of a square using '#' characters
            and spaces
        """
        if self.__size == 0:
            return ""
        str_1 = "\n" * self.__position[1]
        str_2 = "\n".join([" " * self.__position[0]
                          + "#" * self.__size for i in range(self.size)])
        return str_1 + str_2
