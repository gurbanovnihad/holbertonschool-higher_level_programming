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

    @classmethod
    def create(cls, **dictionary):
        '''
        This function returns an instance with all attributes already set
        '''
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Square:
            new_instance = Square(5)
        if cls is Rectangle:
            new_instance = Rectangle(5, 9)
        try:
            new_instance.update(**dictionary)
        except Exception:
            pass
        return new_instance

    @classmethod
    def load_from_file(cls):
        '''  This function returns a list of instances '''
        new_list = []
        try:
            filename = "{}.json".format(cls.__name__)
            with open(filename, "r", encoding="utf-8") as f:
                data = f.read()
                list_json = cls.from_json_string(data)
                try:
                    for dict_ in list_json:
                        new_list.append(cls.create(**dictionary))
                except Exception:
                    pass
            f.close()
        except Exception:
            pass
        finally:
            return new_list
