#!/usr/bin/python3
"""Student to JSON
Class definition for Student
"""


class Student:
    """Student to JSON

    Defines a student
    """

    def __init__(self, first_name, last_name, age):
        """Instantiates a student

        Args:
            first_name (str): A student's first name
            last_name (str): A student's last name
            age (int): A student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method

        Returns:
            A dictionary representation of a Student instance
        """
        return self.__dict__
