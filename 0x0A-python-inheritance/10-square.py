#!/usr/bin/python3
Rectangle = __import__("9-rectangle").Rectangle
"""Square module"""


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):

        self.integer_validator("Square", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f"[Rectangle] {self.__size}/{self.__size}"
