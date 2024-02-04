#!/usr/bin/python3
'''
    Module for dividing matrices to integers
'''


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number.

    Args:
        matrix (list of lists): Matrix of integers or floats.
        div (int or float): Divisor.

    Returns:
        list of lists: New matrix with elements divided by div,
        rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats,
                   or if each row of the matrix does not have the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is equal to 0.

    Example:
        >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    """
    # Check if matrix is a list of lists of integers/floats
    matrix_check = True
    for row in matrix:
        i_check = isinstance(row, list)
        if not i_check or any(not isinstance(el, (int, float)) for el in row):
            matrix_check = False
            break
    if not matrix_check:
        raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")

    # Check if each row has the same size
    size_check = True
    for row in matrix:
        if len(row) != len(matrix[0]):
            size_check = False
            break
    if not size_check:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div isi not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div, round to 2 decimal places
    new_matrix = [[round(el / div, 2) for el in row] for row in matrix]

    return new_matrix
