#!/usr/bin/python3
"""First Rectangle
Class definition for Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """First Rectangle
    Defines a rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiates a rectangle instance

        Args:
            id (int): optional argument for id attribute

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieves the width"""
        return self.__width

    @width.setter
    def width(self, val):
        """Sets the width of a rectangle"""
        self.__width = val

    @property
    def height(self):
        """Retrieves the height"""
        return self.__height

    @height.setter
    def height(self, val):
        """Sets the height of a rectangle"""
        self.__height = val

    @property
    def x(self):
        """Retrieves the x attribute of a rectangle"""
        return self.__x

    @x.setter
    def x(self, val):
        """Sets the x attribute of a rectangle"""
        self.__x = val

    @property
    def y(self):
        """Retrieves the y attribute of a rectangle"""
        return self.__y

    @y.setter
    def y(self, val):
        """Sets the y attribute of a rectangle"""
        self.__y = val
