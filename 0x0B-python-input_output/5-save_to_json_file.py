#!/usr/bin/python3
"""Save Object to a file
Function definition for save_to_json_file"""


def save_to_json_file(my_obj, filename):
    """To JSON string

    A function that writes an Object to a text file,
    using a JSON representation

    Exceptions are not managed if the object can’t be serialized.
    File permission exceptions are not managed.

    Args:
        my_obj: The object
        filename (str): The text filename

    """
    import json
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
