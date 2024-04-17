#!/usr/bin/python3
"""write file module"""


def write_file(filename="", text=""):
    """write file function"""
    with open(filename, "w", encoding="UTF8") as file:
        file.write(text)
