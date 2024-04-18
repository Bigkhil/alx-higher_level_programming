#!/usr/bin/python3
"""add arguments to python list then save to a file"""
import sys
save_to_json_file = __import__("save_to_json_file").save_to_json_file
load_from_json_file = __import__("load_from_json_file").load_from_json_file


args = list(sys.argv[1:])
my_list = []
try:
    my_list = load_from_json_file(add_item.json)
except Exception:
    pass
my_list += args
save_to_json_file(my_list, add_item.json)
