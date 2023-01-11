#!/usr/bin/python3

"""Roman to Integer

A module that defines a function,
that converts a Roman numeral to an integer
"""


def roman_to_int(roman_string):
    """Roman to Integer

    A function that converts a Roman numeral to an integer.
    You can assume the number will be between 1 to 3999.
    If the roman_string is not a string or None, return 0

    Args:
        roman_string (str): The Roman numeral

    Returns:
        The integer representation of the roman numeral
    """
    if type(roman_string) != str or roman_string is None:
        return 0
    # a dictionary for the roman numerals
    key = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # create a list of each letter in roma_string in its number form
    list1 = [key[i] for i in roman_string]
    # to compare each element in list1 with the next element
    # 0 is made to follow the last element
    list2 = list1[1:] + [0]
    # list1 but where element = -element when it is less than the next
    list3 = [-i if i < j else i for i, j in zip(list1, list2)]
    # sum of all elements in list3 is the required integer
    return sum(list3)
