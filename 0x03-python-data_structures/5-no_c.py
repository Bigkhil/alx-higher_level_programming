#!/usr/bin/python3
def no_c(my_string):
    new_str = []
    if my_string:
        for i in my_string:
            if my_string[i] != 'c' or my_string[i] != 'C':
                new_str.append(my_string[i])
        return new_str
