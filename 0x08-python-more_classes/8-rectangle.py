#!/usr/bin/python3
""" This module contains a class definition for a rectangle
    with methods to find the perimeter and area of the rectangle
    and str, repr and del methods.
    Public class attribute number_of_instances:
        Initialized to 0
        Incremented during each new instance instantiation
        Decremented during each instance deletion
    Public class attribute print_symbol:
        Initialized to #
        Used as symbol for string representation
        Can be any type
    Static method def bigger_or_equal that returns the biggest
    rectangle based on the area
"""


class Rectangle:
    """ A class definition for a rectangle """
    number_of_instances = 0
    """int: initialized to zero"""
    print_symbol = '#'
    """Used as symbol for string representation
       Can be any type
    """

    def __init__(self, width=0, height=0):
        """ Instantiates the rectangle """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1
        """Incremented during each new instance instantiation"""

    def __str__(self):
        """ Returns a string that uses the character(s)
            stored in print_symbol character to represent the rectangle.
            If width or height is equal to 0, it returns an empty string
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join(str(self.print_symbol) * self.__width for i in range(
                        self.__height))

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
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
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
        if value < 0:
            raise ValueError('height must be >= 0')
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method that returns the biggest rectangle based on the area

        Args:
            rect_1: must be an instance of Rectangle
            rect_2: must be an instance of Rectangle

        Returns:
                the biggest rectangle based on the area,
                or rect_1 if both have the same area value
        """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError('rect_2 must be an instance of Rectangle')
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            return rect_2
