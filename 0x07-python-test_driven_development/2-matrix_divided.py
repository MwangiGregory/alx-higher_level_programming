#!/usr/bin/python3
"""This module defines function matrix_divided"""


def matrix_divided(matrix, div):
    """Divides all the elements of a matrix"""

    err_mes = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(err_mes)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(err_mes)
        for item in row:
            if type(item) not in [int, float]:
                raise TypeError(err_mes)

    row_sizes = [len(row) for row in matrix]
    first_element = row_sizes[0]
    for i in row_sizes:
        if i != first_element:
            raise TypeError('Each row of the matrix must have the same size')

    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by Zero')

    new_matrix = []
    for row in matrix:
        temp_list = []
        for item in row:
            result = round(item / div, 2)
            temp_list.append(result)

        new_matrix.append(temp_list[:])

    return (new_matrix)
