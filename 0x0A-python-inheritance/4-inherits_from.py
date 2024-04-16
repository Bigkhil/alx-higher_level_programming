#!/usr/bin/python3
"""issubclass module"""


def inherits_from(obj, a_class):
    """issubclass function"""
    if type(obj) is a_class:
        return False
    return issubclass(obj, a_class)
