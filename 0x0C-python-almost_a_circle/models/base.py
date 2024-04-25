#!/usr/bin/python3
"""Base class"""
import os.path
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
            self.id = self.__nb_objects

    def to_json_string(list_dictionaries):
        """to json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file"""
        filename = cls.__name__ + ".json"
        list = []
        if list_objs is not None:
            for obj in list_objs:
                list.append(obj.to_dictionary())
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON"""
        import json
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create method"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """Load from file"""
        filename = cls.__name__ + ".json"
        new_list = []
        if os.path.exists(filename):
            with open(filename, "r") as f:
                new_list = cls.from_json_string(f.read())
            for dict in new_list:
                new_list.append(cls.create(**dict))
        return new_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to file csv"""
        filename = cls.__name__ + ".csv"
        list = []
        if list_objs is not None:
            for obj in list_objs:
                list.append(obj.to_dictionary())
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list))
