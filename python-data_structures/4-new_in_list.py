#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    duplicate_list = my_list.copy()

    if idx < 0 or idx >= len(duplicate_list):
        return duplicate_list
    else:
        duplicate_list[idx] = element
        return duplicate_list
