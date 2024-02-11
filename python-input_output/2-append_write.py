#!/usr/bin/python3
'''Module Doc'''


def append_write(filename="", text=""):
    '''Function Doc'''

    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
