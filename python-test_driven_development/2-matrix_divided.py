#!/usr/bin/python3
"""
This function divides a matrix
"""


def matrix_divided(matrix, div):
    """
    Parameters:
        matrix: matrix to be divided
        div: number to be divided

    Returns:
        returns a new matrix divied by div

    """
    if type(matrix) is not list:
        raise TypeError("matrix must be matrix (list/lists) of integers/floats")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in matrix:
        if type(i) is not list:
            raise TypeError("matrix must matrix (list/lists) of integers/floats")

        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        for j in i:
            if type(j) not in [int, float]:

                raise TypeError("matrix must matrix (lists/lists) integers/floats")

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return new_matrix
