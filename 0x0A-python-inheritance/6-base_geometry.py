#!/usr/bin/python3
"""Class definition for BaseGeometry"""


class BaseGeometry:
    """A class with a public instance method that raises an exception"""
    def area(self):
        """A public instance method

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")
