#!/usr/bin/python3
str_end = ", "

for number in range(100):
    if number == 99:
        str_end = "\n"
    print("{:02d}".format(number), end=str_end)
