#!/usr/bin/python3
"""read file module"""


def read_file(filename="", encoding='utf-8'):
    """read file function"""
    with open(filename) as file:
        print(file.read(), end="")
