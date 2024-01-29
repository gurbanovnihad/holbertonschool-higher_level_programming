#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for list_ in matrix:
        squared_list = list(map(lambda x: x ** 2, list_))
        square_matrix.append(squared_list)

    return square_matrix
