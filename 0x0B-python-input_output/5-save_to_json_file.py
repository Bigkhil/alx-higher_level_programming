#!/usr/bin/python3
"""json file deserialization"""
import json


def save_to_json_file(my_obj, filename):
    """json file function"""
    with open(filename, 'w') as file:
        data = json.dumps(my_obj)
        file.write(data)
