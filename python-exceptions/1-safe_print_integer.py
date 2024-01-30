#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, int) or (isinstance(value, bool) and value):
            print("{:d}".format(int(value)))
            return True
    except (ValueError, TypeError):
        return False
