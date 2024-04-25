#!/usr/bin/python3
"""Base class"""
import json
from .rectangle import Rectangle
from .square import Square


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
