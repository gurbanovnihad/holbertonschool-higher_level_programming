#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            row_end = " "
            if i == len(row) - 1:
                row_end = ""
            print("{:d}".format(row[i]), end=row_end)
        print()
