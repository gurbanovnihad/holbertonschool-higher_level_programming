#!/usr/bin/python3

def no_c(my_string):
    no_c_str = ""
    for char in my_string:
        if char not in ["c", "C"]:
            no_c_str += char
    return no_c_str
