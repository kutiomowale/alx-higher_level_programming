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
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """Retrieves the height"""
        return self.__height

    @height.setter
    def height(self, val):
        """Sets the height of a rectangle"""
        if type(val) is not int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        """Retrieves the x attribute of a rectangle"""
        return self.__x

    @x.setter
    def x(self, val):
        """Sets the x attribute of a rectangle"""
        if type(val) is not int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """Retrieves the y attribute of a rectangle"""
        return self.__y

    @y.setter
    def y(self, val):
        """Sets the y attribute of a rectangle"""
        if type(val) is not int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """Returns the area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.__x, self.__y,
                        self.__width, self.__height))
