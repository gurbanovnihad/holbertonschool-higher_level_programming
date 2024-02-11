#!/usr/bin/python3
'''Module Doc'''


import json


def load_from_json_file(filename):
    '''Function Doc'''
    with open(filename) as f:
        for line in f:
            data = json.loads(line)
    return data
