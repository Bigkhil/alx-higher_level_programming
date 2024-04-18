#!/usr/bin/python3
"""json file deserialization"""
import json


def load_from_json_file(filename):
    """json file function"""
    with open(filename, 'r') as file:
        """reads the object from the file as string then returns it as object"""
        data = file.read()
        return json.loads(data)
