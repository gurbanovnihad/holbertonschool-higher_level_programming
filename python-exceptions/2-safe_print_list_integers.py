#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        i = 0
        cnt_int = 0

        while i < x:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                cnt_int += 1
            i += 1
    except (ValueError, TypeError):
        return
    else:
        print()
        return cnt_int
