#!/usr/bin/python3
"""class base"""
import json
from .rectangle import Rectangle
from .square import Square


class Base:
    """class Base doc"""
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
        """converts the list of dictionaries to json string"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves the json string to file"""
        if list_objs is not None:
            if isinstance(list_objs[0], Rectangle):
                with open('Rectangle.json', 'w') as file:
                    for i in list_objs:
                        file.write(cls.to_json_string(i))
            else:
                with open('Square.json', 'w') as file:
                    for i in list_objs:
                        file.write(cls.to_json_string(i))
        else:
            pass
