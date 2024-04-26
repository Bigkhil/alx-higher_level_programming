#!/usr/bin/python3
"""Base class"""
import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Base Class
        Args:
            id (int): id of the object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to json string"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file"""
        file_name = cls.__name__ + ".json"
        with open(file_name, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = []
                for i in list_objs:
                    list_dicts.append(i.to_dictionary())
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """from json string to list"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create instance method"""
        instance = None
        if cls.__name__ == "Rectangle":
            instance = cls(5, 5)
        else:
            instance = cls(5)
        instance.update(**dictionary)
        return instance
