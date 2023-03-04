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
        width, height = size, size
        super().__init__(width, height, x, y, id)

    def __str__(self):
        """Returns [Square] (<id>) <x>/<y> - <size>
        where size is the width or height"""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.__x, self.__y,
                        self.__width))
