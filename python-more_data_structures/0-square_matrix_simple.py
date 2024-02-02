#!/usr/bin/python3
#function that computes square values in a matrix
def square_matrix_simple(matrix=[]):
    #we can use map
    squaredMatrix = list(map(lambda row: list(map(lambda x: x**2, row)), matrix))
    return squaredMatrix
