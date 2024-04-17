#!/usr/bin/python3
"""write file module"""


def write_file(filename="", text=""):
    """write file function"""
    with open(filename, "w", encoding='utf-8') as file:
        return file.write(text)
