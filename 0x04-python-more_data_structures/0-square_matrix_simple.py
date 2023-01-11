#!/usr/bin/python3

"""A function that computes the square value of all integers of a matrix"""


def square_matrix_simple(matrix=[]):
    """The function

    Args:
        matrix (list): The matrix

    Returns:
        list: a new matrix, Same size as matrix
              Each value should be the square of the value of the input
    """
    return [[j**2 for j in i] for i in matrix]
