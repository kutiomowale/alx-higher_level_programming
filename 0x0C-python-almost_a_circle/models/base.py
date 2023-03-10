#!/usr/bin/python3
"""Base class
Class definition for Base
"""
import json


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
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if type(list_dictionaries) is not list:
            return
        for dic in list_dictionaries:
            if type(dic) is not dict:
                return
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file:

        Args:
        list_objs (list): is a list of instances who inherits of Base
        - example: list of Rectangle or list of Square instances
        If list_objs is None, save an empty list
        The filename must be: <Class name>.json - example: Rectangle.json
        The static method to_json_string is used
        The file is overwritten if it already exists
        """
        new_list = []
        if list_objs:
            for obj in list_objs:
                if isinstance(obj, Base):
                    new_list.append(obj.to_dictionary())
        json_dictionary = cls.to_json_string(new_list)
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(json_dictionary)

    @staticmethod
    def from_json_string(json_string):
        """Static method returns the listof
        the JSON string representation json_string:

        Args:
            json_string (str): is a string representing a list of dictionaries

        Returns:
            An empty list, If json_string is None or empty
            Otherwise, it return the list represented by json_string
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Class method that returns an instance with all attributes
        already set

        It does this by creating a “dummy” instance i.e.
        a Rectangle or Square instance with “dummy”
        mandatory attributes (width, height, size, etc.)

        It then calls the update instance method to this “dummy” instance
        to apply your real values

        Args:
            **dictionary can be thought of as a double pointer to a dictionary

        Returns:
            The new instance
        """
        new_obj = cls(5, 5)
        new_obj.update(**dictionary)
        return new_obj
