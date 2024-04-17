#!/usr/bin/python3
"""append file module"""


def append_write(filename="", text=""):
    """append file function"""
    with open(filename, "a", encoding='utf-8') as file:
        return file.write(text)
