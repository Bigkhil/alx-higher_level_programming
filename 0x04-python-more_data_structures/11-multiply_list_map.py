#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new = my_list[:]
    w = map(lambda x: x * number, new)
    return list(w)
