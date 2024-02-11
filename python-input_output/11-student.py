#!/usr/bin/python3
'''Module Doc'''


class Student:
    '''Class Doc'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__

    def to_json(self, attrs=None):
        if type(attrs) is list:
            new_dict = {}
            for key_dict in self.__dict__:
                for key_list in attrs:
                    if key_dict == key_list:
                        new_dict[key_dict] = self.__dict__[key_list]
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        for key in json:
            if key == "first_name":
                self.first_name = json[key]
            if key == "last_name":
                self.last_name = json[key]
            if key == "age":
                self.age == json[key]
