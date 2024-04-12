#!/usr/bin/python3
"""square module"""


class Square:
    """defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        for i in range(2):
            if type(position[i]) is not int:
                raise TypeError
                ("position must be a tuple of 2 positive integers")
            elif position[i] < 0:
                raise TypeError
                ("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        """this is getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """this is setter"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        for i in range(2):
            if type(value[i]) is not int:
                raise TypeError
                ("position must be a tuple of 2 positive integers")
            elif value[i] < 0:
                raise TypeError
                ("position must be a tuple of 2 positive integers")
