#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    end = " "
    for row in matrix:
        for integer in row:
            if row.index(integer) == len(row) - 1:
                end = ""
            print("{:d}".format(integer), end=" ")
        print()
