#!/usr/bin/python3
"""read file module"""


def read_file(filename=""):
    """read file function"""
    with open(filename) as file:
        for line in file:
            print(line.strip())
