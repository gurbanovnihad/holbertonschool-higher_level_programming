#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_n = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }

    if (type(roman_string) is not str) or (not roman_string):
        return 0

    int_num = 0

    for i in range(len(roman_string)):
        if i < len(roman_string) - 1 and\
                roman_n[roman_string[i]] < roman_n[roman_string[i + 1]]:
            int_num -= roman_n[roman_string[i]]
        else:
            int_num += roman_n[roman_string[i]]

    return int_num
