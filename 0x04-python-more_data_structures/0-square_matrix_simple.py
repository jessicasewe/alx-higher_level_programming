#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = matrix.copy()
    for integer in  range(len(matrix)):
        square_matrix[integer] = list(map(lambda i:i**2,(matrix[integer])))
    return square_matrix
