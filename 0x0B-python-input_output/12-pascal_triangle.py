#!/usr/bin/python3
"""Pascal's Triangle
Function definition for pascal_triangle
"""


def pascal_triangle(n):
    """Pascal's Triangle

    A function that that returns a list of lists of integers
    representing the Pascal’s triangle of n
    It is assumed that n will be always an integer

    Args:
        n (int): The number

    Returns:
        list: an empty list if n <= 0
        Otherwise, the required list

    """
    p_list = []
    """list: The required list"""
    if n <= 0:
        return p_list
    p_list.append([1])
    for j in range(n - 1):
        # Append next list based on the last list of lists
        # i.e based on p_list[-1]
        # Do this n - 1 times
        new_row = [1]
        # 1 is always the first integer
        """list: New list to append"""
        i = 0
        """int: Index of previous integer"""
        for element in (p_list[-1][1:]):
            new_row.append(element + p_list[-1][i])
            # Add next integer to previous integer to get new integer to append
            # to new_row
            i += 1
        new_row.append(1)
        # 1 is also always the last integer
        p_list.append(new_row)
    return p_list
