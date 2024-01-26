#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argument_list = sys.argv
    argument_count = len(sys.argv)

    if argument_count == 1:
        print("{} arguments.".format(argument_count - 1))
    elif argument_count == 2:
        print("{} argument:".format(argument_count - 1))
    else:
        print("{} arguments:".format(argument_count))
        for i in range(1, argument_count):
            print("{}: {}".format(i, argument_list[i]))
