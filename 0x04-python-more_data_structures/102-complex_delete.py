#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_delete = []
    for i in a_dictionary.keys():
        if a_dictionary[i] is not None and a_dictionary[i] == value:
            keys_to_delete.append(i)
    for i in keys_to_delete:
        del (a_dictionary[i])
    return a_dictionary
