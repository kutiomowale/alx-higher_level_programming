#!/usr/bin/python3
"""MyList class definition"""


class MyList(list):
    """A class MyList that inherits f_rom list

    It is assumed that all the elements of the list will be of type int

    """
    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
