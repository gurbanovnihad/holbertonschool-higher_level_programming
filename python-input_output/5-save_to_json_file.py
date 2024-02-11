#!/usr/bin/python3
'''Module Doc'''

import json


def save_to_json_file(my_obj, filename):
    '''Function Doc'''
    with open(filename, "w") as f:
        json.dump(my_obj, f)
