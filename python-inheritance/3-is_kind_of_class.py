#!/usr/bin/python3
'''Module Doc'''


def is_kind_of_class(obj, a_class):
    '''Function doc'''

    return issubclass(type(obj), a_class) and type(obj) != a_class
