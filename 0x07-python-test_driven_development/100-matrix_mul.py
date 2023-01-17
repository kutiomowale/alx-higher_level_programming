#!/usr/bin/python3
"""Matrix multiplication
This module is for the matrix_mul funtion

The function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """A function that multiplies 2 matrices

    Args:
        m_a (list): The first matrix
        m_b (list): The second matrix

    Returns:
        A new matrix a new matrix, which is the matrix multiplication of the
        two matrices

    Raises:
        TypeError: If m_a or m_b is not a list of lists of integers or floats
        TypeError: If Each row of m_a or m_b are not of the same size
        ValueError: If m_a and m_b can’t be multiplied
    """
    # Check if m_a is a valid matrix
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    for row in m_a:
        if type(row) != list:
            raise TypeError("m_a must be a list of lists")
        if len(row) == 0:
            raise ValueError("m_a can't be empty")
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    size = len(m_a[0])
    for row in m_a:
        if len(row) != size:
            raise TypeError("each row of m_a must be of the same size")

    # Check if m_b is a valid matrix
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for row in m_b:
        if type(row) != list:
            raise TypeError("m_b must be a list of lists")
        if len(row) == 0:
            raise ValueError("m_b can't be empty")
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
    size = len(m_b[0])
    for row in m_b:
        if len(row) != size:
            raise TypeError("each row of m_b must be of the same size")

    # Check that m_a and m_b can be multiplied i.e
    # number of columns in m_a is equal to number of rows in m_b
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
