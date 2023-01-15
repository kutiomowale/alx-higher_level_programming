#!/usr/bin/python3

"""A function that prints a given name"""


def say_my_name(first_name, last_name=""):
    """Say my name

    A function that prints My name is <first name> <last name>

    Args:
        first_name (str) : The first name
        last_name (str) : The last name(optional)
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
