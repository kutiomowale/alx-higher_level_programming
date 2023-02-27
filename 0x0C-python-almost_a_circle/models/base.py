#!/usr/bin/python3
"""Base class
Class definition for Base
"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiates a Base instance

        Args:
            id (int): optional argument for id attribute

        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
