#!/usr/bin/python3
"""Base class"""
import json
import os
import csv


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

    @classmethod
    def load_from_file(cls):
        """returns list of instances from class_name.json"""
        file_name = cls.__name__ + ".json"
        list_dictionaries = []
        list_instances = []
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                list_dictionaries = cls.from_json_string(file.read())
            for i in list_dictionaries:
                list_instances.append(cls.create(**i))
            return list_instances
        else:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to file csv"""
        mycsv = ""
        flag = -1
        for o in list_objs:
            if o.__class__.__name__ == "Rectangle":
                if flag == -1:
                    mycsv += "id,width,height,x,y\n"
                    flag = 0

                mycsv += f"{o.id},{o.width},{o.height},{o.x},{o.y}\n"

            else:
                if flag == -1:
                    mycsv += "id,size,x,y\n"
                    flag = 0

                mycsv += f"{o.id},{o.size},{o.x},{o.y}\n"

        with open(cls.__name__+".csv", encoding="utf-8", mode="w") as file:
            file.write(mycsv[:-1])

    @classmethod
    def load_from_file_csv(cls):
        """load from file csv"""
        data = []
        with open(cls.__name__+".csv", encoding="utf-8", mode="r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Convert values to integers
                for key in row:
                    row[key] = int(row[key])
                data.append(row)
        return list(map(lambda obj: cls.create(**obj), data))
