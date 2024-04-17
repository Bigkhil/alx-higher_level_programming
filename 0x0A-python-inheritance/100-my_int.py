#!/usr/bin/python3
"""Module for BaseGeometry class"""


class MyInt(int):
    """MY ITN CLASS"""

    def __eq__(self, value):
        """Returns the opposite of the == operator"""
        return super().__ne__(value)

    def __ne__(self, value):
        """Returns the opposite of the != operator"""
        return super().__eq__(value)
