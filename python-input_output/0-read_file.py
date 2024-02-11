#!/usr/bin/python3
'''Module Doc'''


def read_file(filename=""):
    '''Function reads files line by line'''

    with open(filename) as f:
        for line in f:
            print(line, end="")
