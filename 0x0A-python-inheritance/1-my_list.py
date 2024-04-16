#!/usr/bin/python3
"""mylist module"""


class MyList(list):
    """class Mylist"""
    def print_sorted(self):
        print(sorted(self))
