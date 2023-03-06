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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): Is a list of dictionaries

        Returns:
            If list_dictionaries is None or empty, return the string: "[]"
            Otherwise, return the JSON string representation of
            list_dictionaries
        """
        import json
        if list_dictionaries and len(list_dictionaries) > 0:
            return json.dumps(list_dictionaries)
        return "[]"
