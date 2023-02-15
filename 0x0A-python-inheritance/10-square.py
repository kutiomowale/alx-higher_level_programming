#!/usr/bin/python3
"""Class definition for Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class Square that inherits from Rectangle"""
    def __init__(self, size):
        """Initializes a square"""
        super().__init__(size, size)
        self.__size = size
