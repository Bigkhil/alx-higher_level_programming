#!/usr/bin/python3
"""Student class module"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            d = self.__dict__
            ret = {}
            for x in attrs:
                if x in d:
                    ret[x] = d[x]
            return ret
        return self.__dict__
