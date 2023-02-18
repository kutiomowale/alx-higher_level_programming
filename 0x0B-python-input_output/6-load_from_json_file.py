#!/usr/bin/python3
"""Create object from a JSON file
Function definition for load_from_json_file
"""


def load_from_json_file(filename):
    """Create object from a JSON file

    A function that creates an Object from a “JSON file”

    Exceptions are not managed if the JSON string
    doesn’t represent an object.
    File permissions/exceptions are not managed.

    Args:
        my_obj: The object
        filename (str): The JSON filename

    """
    import json
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
