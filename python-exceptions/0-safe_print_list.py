#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    real_n = ''
    try:
        i = 0
        while i < x and my_list[i]:
            real_n += str(my_list[i])
            i += 1
        print(real_n)
        return i

    except IndexError:
        real_n = ''
        for i in my_list:
            real_n += str(i)
        print(real_n)
        return i
