#!/usr/bin/python3
'''Module Doc'''


def write_file(filename="", text=""):
    '''Function Doc'''

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

    return len(text)
