#!/usr/bin/python3
'''
This module is for practising test driven development
'''


def add_integer(a, b=98):
    '''
    add_integer function adds to integer and returns as an integer

    Args:
        a (int or float): The first number.
        b (int or float): The second number. Default is 98.

    Returns:
        sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    '''

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    result = a + b

    return result
