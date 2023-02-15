#!/usr/bin/python3
"""Class definition for BaseGeometry"""


class BaseGeometry:
    """A class with a method area that raises an exception

    And a method integer_validator that validates a value

    """
    def area(self):
        """A public instance method

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A public instance method that validates a value

        Raises:
            TypeError: If `value` is not an integer
            ValueError: If `value` is less or equal to 0

        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
