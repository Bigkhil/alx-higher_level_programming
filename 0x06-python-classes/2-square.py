#!/usr/bin/python3
"""square module"""


class Square:
    """defines a square"""
    def __init__(self, size):
        if size is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
