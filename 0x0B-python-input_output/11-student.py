#!/usr/bin/python3
"""Student to disk and reload
Class definition for Student
"""


class Student:
    """Student to disk and reload

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
            Otherwise, all attributes must be retrieved

        Returns:
            A filtered dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        return {attr: self.__dict__[attr] for attr in attrs
                if attr in self.__dict__}

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance:

        It is assumed that json will always be a dictionary
        A dictionary key will be the public attribute name
        A dictionary value will be the value of the public attribute

        Args:
            json (dict): A dictionary used in replacing the attributes of a
            student
        """
        for key in json:
            if key in self.__dict__:
                self.__dict__[key] = json[key]
