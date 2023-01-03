#!/usr/bin/python3
""" This module contains a class definition for a rectangle """


class Rectangle:
    """ A class definition for a rectangle """
    def __init__(self, width=0, height=0):
        """ Instantiates the rectangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrieves the width of the rectangle
            value is the width to be set
            width must be an integer
            width must be greater than or equal to zero
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """ Retrieves the height of the rectangle
            value is the height to be set
            height must be an integer
            height must be greater than or equal to zero
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
