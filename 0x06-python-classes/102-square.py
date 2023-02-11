#!/usr/bin/python3
"""A class that defines a square"""


class Square:
    """A class that defines a square, with a method for square area
       Square instance can answer to comparators:
       ==, !=, >, >=, < and <= based on the square area
    """
    def __init__(self, size=0):
        """Initializes the square"""
        self.__size = size

    @property
    def size(self):
        """Returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        if type(value) not in [int, float]:
            raise TypeError("size must be a number")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the current square area"""
        return self.__size * self.__size

    def __eq__(self, other):
        """Square instance can answer to == comparator,
           based on the square area
        """
        if isinstance(other, Square):
            return self.area() == other.area()

    def __ne__(self, other):
        """Square instance can answer to != comparator,
           based on the square area
        """
        if isinstance(other, Square):
            return self.area() != other.area()

    def __gt__(self, other):
        """Square instance can answer to > comparator,
           based on the square area
        """
        if isinstance(other, Square):
            return self.area() > other.area()

    def __ge__(self, other):
        """Square instance can answer to >= comparator,
           based on the square area
        """
        if isinstance(other, Square):
            return self.area() >= other.area()

    def __lt__(self, other):
        """Square instance can answer to < comparator,
           based on the square area
        """
        if isinstance(other, Square):
            return self.area() < other.area()

    def __le__(self, other):
        """Square instance can answer to <= comparator,
           based on the square area
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
