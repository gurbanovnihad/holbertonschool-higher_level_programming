#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    row_end = " "
    for row in matrix:
        for integer in row:
            if row.index(integer) == len(row) - 1:
                row_end = ""
            print("{:d}".format(integer), end=row_end)
        print()
