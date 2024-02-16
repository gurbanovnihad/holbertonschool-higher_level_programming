#!/usr/bin/python3
'''Base Module Doc'''


import json


class Base:
    '''Base Class'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        This method returns the JSON string representation
        of list_dictionaries
        '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''
        returns the list of the JSON string representation json_string
        '''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        This method writes the JSON string representation
        of list_objs to a file
        '''
        list_dict = None
        list_dict = [obj.to_dictionary() for obj in list_objs]\
            if list_objs else []
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dict))
