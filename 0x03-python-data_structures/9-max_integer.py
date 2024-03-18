#!/usr/bin/python3
def max_integer(my_list=[]):
    mx = None
    if my_list:
        for i in my_list:
            if i > mx:
                mx = i
    return mx
