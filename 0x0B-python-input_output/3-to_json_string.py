#!/usr/bin/python3
"""To JSON string
Function definition for to_json_string"""


def to_json_string(my_obj):
    """To JSON string

    A function that returns the JSON representation of an object (string)

    Exceptions are not managed if the object can’t be serialized.
    and returns the number of characters added.

    Args:
        my_obj: The object

    Returns:
        The JSON representation of the object

"""
    import json
    return json.dumps(my_obj)
