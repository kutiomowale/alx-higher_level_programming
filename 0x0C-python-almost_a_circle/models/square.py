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
