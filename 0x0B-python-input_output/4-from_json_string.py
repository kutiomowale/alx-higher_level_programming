#!/usr/bin/python3
"""From JSON string to Object
Function definition for from_json_string"""


def from_json_string(my_str):
    """To JSON string

    A function that returns an object (Python data structure)
    represented by a JSON string

    Exceptions are not managed if the JSON string doesn’t represent an object.

    Args:
        my_str: The JSON string

    Returns:
        The object

"""
    import json
    return json.loads(my_str)
