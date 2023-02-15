#!/usr/bin/python3
"""Class definition for Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class Square that inherits from Rectangle"""
    def __init__(self, size):
        """Initializes a square"""
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """Returns a description of the square:
        """
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
