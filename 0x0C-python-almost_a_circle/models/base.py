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
        if cls.__name__ == "Square":
            new_obj = cls(1)
        else:
            new_obj = cls(1, 1)
        new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def load_from_file(cls):
        """Class method that returns a list of instances

        The filename must be: <Class name>.json - example: Rectangle.json
        The from_json_string method is used to convert the json string
        read from the file to a list while
        The create method is used to create the required instances

        Returns:
            An empty list, if the file doesn't exist
            Otherwise, return a list of instances - the type of these
            instances depends on cls (current class using this method)
        """
        try:
            with open("{}.json".format(cls.__name__), "r",
                      encoding="utf-8") as f:
                text = f.read()
                list_text = cls.from_json_string(text)
                list_text_objs = [cls.create(**dic) for dic in list_text]
                return list_text_objs
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the csv representation of list_objs to a file:

        Format of the CSV:
        Rectangle: <id>,<width>,<height>,<x>,<y>
        Square: <id>,<size>,<x>,<y>

        Args:
        list_objs (list): is a list of instances who inherits of Base
        - example: list of Rectangle or list of Square instances
        If list_objs is None, save an empty list
        The filename must be: <Class name>.csv - example: Rectangle.csv
        The file is overwritten if it already exists
        """
        new_list = []
        if list_objs:
            for obj in list_objs:
                if isinstance(obj, Base):
                    if cls.__name__ == "Rectangle":
                        new_list.append("{},{},{},{},{}\n".format(obj.id,
                                        obj.width, obj.height, obj.x, obj.y))
                    if cls.__name__ == "Square":
                        new_list.append("{},{},{},{}\n".format(obj.id,
                                        obj.size, obj.x, obj.y))
        csv_string = "".join(new_list)
        with open("{}.csv".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(csv_string)

    @classmethod
    def load_from_file_csv(cls):
        """Class method that returns a list of instances
        generated from a csv file

        The filename must be: <Class name>.csv - example: Rectangle.csv

        Returns:
            An empty list, if the file doesn't exist
            Otherwise, return a list of instances - the type of these
            instances depends on cls (current class using this method)
        """
        try:
            with open("{}.csv".format(cls.__name__), "r",
                      encoding="utf-8") as f:
                csv_list = list(f)
                if len(csv_list) == 0:
                    return []
                req_list = []
                for i in csv_list:
                    temp_list = i.split(",")
                    temp_list = [int(j) for j in temp_list]
                    if cls.__name__ == "Rectangle":
                        new_obj = cls(temp_list[1], temp_list[2], temp_list[3],
                                      temp_list[4], temp_list[0])
                        req_list.append(new_obj)
                    if cls.__name__ == "Square":
                        new_obj = cls(temp_list[1], temp_list[2], temp_list[3],
                                      temp_list[0])
                        req_list.append(new_obj)

                return req_list
        except FileNotFoundError:
            return []
