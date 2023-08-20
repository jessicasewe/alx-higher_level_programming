#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda number: list(map(lambda number2: number2**2, number)), matrix)))
