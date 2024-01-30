#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if int(value) and value != True:
            print("{:d}".format(value))
            return True
    except ValueError:
        return False
