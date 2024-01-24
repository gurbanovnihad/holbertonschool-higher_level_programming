#!/usr/bin/env python3
def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            char_upper = chr(ord(char) - 32)
            print("{}".format(char_upper), end="")
        else:
            print("{}".format(char), end="")
    print("\n")
