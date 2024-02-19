#!/usr/bin/python3
"""
making many division
"""


def matrix_divided(matrix, div):
    """
    A function that divides all elements of a matrix.
    Args:
        matrix (int or float) a list of list
        div (int or float)
    Return:
        A new Matrix
    Raises:
        TypeError
        ZeroDivisionError
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    init_len = len(matrix[0])
    new_matrix = []
    for row in matrix:
        new_row = []
        if init_len != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError('''matrix must be a matrix (list of lists)
                                of integers/float''')
            else:
                new_element = round(element / div, 2)
                new_row.append(new_element)
        new_matrix.append(new_row)
    return new_matrix
