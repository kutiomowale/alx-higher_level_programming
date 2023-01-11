#!/usr/bin/python3

"""Search and replace

A module that defines a function, that replaces all occurrences of an element
by another in a new list.
"""


def search_replace(my_list, search, replace):
    """Search and replace

    A function that replaces all occurrences of an element by another
    in a new list.

    Args:
        my_list: Is the initial list
        search: Is the element to replace in the list
        replace: Is the new element

    Returns:
        new_list: The new list
    """
    return [(replace if i == search else i) for i in my_list]
