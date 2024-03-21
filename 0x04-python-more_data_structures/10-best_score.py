#!/usr/bin/python3
def best_score(a_dictionary):
    if bool(a_dictionary):
        max_value = max(a_dictionary.values())
        for i in a_dictionary.keys():
            if a_dictionary[i] == max:
                return i
    return None
