#!/usr/bin/python3

def remove_char_at(str, n):
    removed_str = ""
    if n >= 0 and n < len(str):
        for i in range(len(str)):
            if i != n:
                removed_str += str[i]
    else:
        removed_str = str
    return removed_str
