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
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not (type(div) in (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return new_matrix
