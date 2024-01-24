#!/usr/bin/env python3
def uppercase(str):
    for index in range(0, len(str)):
        end_str = ""
        if index == len(str) - 1:
            end_str = "\n"

        if ord(str[index]) >= 97 and ord(str[index]) <= 122:
            char_upper = chr(ord(str[index]) - 32)
            print("{}".format(char_upper), end=end_str)
        else:
            print("{}".format(str[index]), end=end_str)
