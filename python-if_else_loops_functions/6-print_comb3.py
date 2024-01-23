#!/usr/bin/python3
str_end = ", "
for i in range(10):
    for j in range(10):
        if i < j:
            if i == 8 and j == 9:
                str_end = "\n"
            print("{}{}".format(i, j), end=str_end)
