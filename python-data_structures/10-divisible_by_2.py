#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return

    bool_list = []

    for i in my_list:
        if i % 2 == 0:
            bool_list.append(True)
        else:
            bool_list.append(False)
    return bool_list
