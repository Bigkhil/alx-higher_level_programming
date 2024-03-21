#!/usr/bin/python3
def best_score(a_dictionary):
    if bool(a_dictionary):
        max = a_dictionary[a_dictionary.keys()[0]]
        ans = a_dictionary.keys()[0]
        for i in a_dictionary.keys():
            if a_dictionary[i] >= max:
                max = a_dictionary[i]
                ans = i
        return ans
    return None
