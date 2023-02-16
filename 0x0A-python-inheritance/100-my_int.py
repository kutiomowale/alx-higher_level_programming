#!/usr/bin/python3
"""Class definition for MyInt"""


class MyInt(int):
    """A class MyInt that inherits from int

    MyInt is a rebel. MyInt has == and != operators inverted

    """
    def __init__(self, value):
        """Initializes an instance"""
        self.value = value

    def __eq__(self, other):
        """Enables an instance to respond to != operator"""
        return self.value != other

    def __ne__(self, other):
        """Enables an instance to respond to == operator"""
        return self.value == other
