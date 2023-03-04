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
        """Sets the width of a rectangle
        Args:
            val (int): The width to set
        """
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
        """Sets the height of a rectangle
        Args:
            val (int): The height to set
        """
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
        """Sets the x attribute of a rectangle
        Args:
            val (int): The value of x to set
        """
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
        """Sets the y attribute of a rectangle
        Args:
            val (int): The value of y to set
        """
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
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.__x, self.__y,
                        self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute

        If *args exists and is not empty:
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        else:
        *kwargs is used,
        where each key represents an attribute to the instance

        Args:
            *args (list): Argument list. Used if it exists and is not empty
            *kwargs (dict): dictionary of attribute-value pairs
        """
        if args is not None and len(args) > 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
            else:
                pass
        else:
            if id in kwargs:
                self.id = kwargs[id]
            if "width" in kwargs:
                self.__width = kwargs["width"]
            if "height" in kwargs:
                self.__height = kwargs["height"]
            if "x" in kwargs:
                self.__x = kwargs["x"]
            if "y" in kwargs:
                self.__y = kwargs["y"]
