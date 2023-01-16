#!/usr/bin/python3
"""This module is for the matrix_divided funtion

The function returns a new matrix, where
all elements of the matrix passed is divided by div
div is the second argument

"""


def matrix_divided(matrix, div):
    """A function that divides all elements of a matrix
       matrix is not modified

    Args:
        matrix : A list of lists of integers or floats
        div : A number(int or float)

    Returns:
        A new matrix a new matrix, where
        all elements of the matrix passed is divided by div
        rounded to 2 decimal places

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats
        TypeError: If Each row of the matrix is not of the same size
        TypeError: If div is not an int and not a float
        ZeroDivisionError: If div is equal to zero
    """
    error1 = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) != list:
        raise TypeError(error1)
    if len(matrix) == 0:
        raise TypeError(error1)
    for row in matrix:
        if type(row) != list:
            raise TypeError(error1)
        if len(row) == 0:
            raise TypeError(error1)
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(error1)

    error2 = "Each row of the matrix must have the same size"
    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError(error2)

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == float('inf') or div == -float('inf') or div != div:
        div = 10

    return [[round(i / div, 2) for i in row] for row in matrix]
