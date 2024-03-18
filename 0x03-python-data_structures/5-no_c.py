#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        new_str = ""
        for i in my_string:
            if my_string[i] != 'c' or my_string[i] != 'C':
                new_str += my_string[i]
        return new_str
