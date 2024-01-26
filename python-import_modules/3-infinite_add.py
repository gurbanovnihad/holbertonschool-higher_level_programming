#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    sum_all = 0

    for i in range(1, len(argv)):
        sum_all += int(argv[i])
    print(sum_all)
