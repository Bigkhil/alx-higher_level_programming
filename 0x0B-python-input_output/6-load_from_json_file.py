#!/usr/bin/python3
"""json file deserialization"""
import json


def load_from_json_file(filename):
    """json file function"""
    with open(filename, 'r') as file:
        return json.loads(file)
