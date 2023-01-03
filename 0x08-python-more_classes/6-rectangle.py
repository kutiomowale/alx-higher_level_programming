#!/usr/bin/python3
""" This module contains a class definition for a rectangle
    with methods to find the perimeter and area of the rectangle
    and str, repr and del methods.
    Public class attribute number_of_instances:
        Initialized to 0
        Incremented during each new instance instantiation
        Decremented during each instance deletion
"""


class Rectangle:
    """ A class definition for a rectangle """
    number_of_instances = 0
    """int: initialized to zero"""

    def __init__(self, width=0, height=0):
        """ Instantiates the rectangle """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1
        """Incremented during each new instance instantiation"""

    def __str__(self):
        """ Returns a string that uses the '#' character to
            represent the rectangle
            if width or height is equal to 0, it returns an empty string
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join("#" * self.__width for i in range(self.__height))

    def __repr__(self):
        """ Returns a string representation of the rectangle to be
            able to recreate a new instance by using eval()
        """
        return "Rectangle(" + str(
                self.__width) + ", " + str(self.__height) + ")"

    def __del__(self):
        """ when an instance of Rectangle is deleted
        """
        type(self).number_of_instances -= 1
        """Decremented during each instance deletion"""
        print("Bye rectangle...")

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
        try:
            if type(value) != int:
                raise TypeError
            if value < 0:
                raise ValueError
        except TypeError:
            print("width must be an integer", end='')
            raise
        except ValueError:
            print("width must be >= 0", end='')
            raise
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
        try:
            if type(value) != int:
                raise TypeError
            if value < 0:
                raise ValueError
        except TypeError:
            print("height must be an integer", end='')
            raise
        except ValueError:
            print("height must be >= 0", end='')
            raise
        else:
            self.__height = value

    def area(self):
        """ Returns the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
