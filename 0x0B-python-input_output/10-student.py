#!/usr/bin/python3
"""Student to JSON with filter
Class definition for Student
"""


class Student:
    """Student to JSON

    Defines a student
    """

    def __init__(self, first_name, last_name, age):
        """Instantiates a Student instance

        Args:
            first_name (str): A student's first name
            last_name (str): A student's last name
            age (int): A student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method

        Args:
            attrs: If attrs is a list of strings, only attribute names
            contained in this list must be retrieved.

        Returns:
            A filtered dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        return {attr: self.__dict__[attr] for attr in attrs
                if attr in self.__dict__}
