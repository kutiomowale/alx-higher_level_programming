#!/usr/bin/python3
"""And now, the Square!
Class definition for Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """And now, the Square!
    Defines a Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiates a Square instance

        Args:
            id (int): optional argument for id attribute

        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieves the size of a square"""
        return self.width

    @size.setter
    def size(self, val):
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.width = val
        self.height = val

    def __str__(self):
        """Returns [Square] (<id>) <x>/<y> - <size>
        where size is the width or height"""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute

        If *args exists and is not empty:
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
        else:
        *kwargs is used,
        where each key represents an attribute to the instance

        Args:
            *args (list): Argument list. Used if it exists and is not empty
            *kwargs (dict): dictionary of attribute-value pairs
        """
        if args is not None and len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle:

        This dictionary must contain:

        id
        size
        x
        y
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
