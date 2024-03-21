#!/usr/bin/python3
def best_score(a_dictionary):
    if bool(a_dictionary):
        max_value = None
        max_key = None
        for key, value in a_dictionary.items():
            if value is not None and (max_value is None or value > max_value):
                max_value = value
                max_key = key
        return max_key
    return None
