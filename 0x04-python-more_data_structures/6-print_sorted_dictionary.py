#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = set()
    for i in a_dictionary.keys():
        new.add(i)
    for i in new:
        print("{}:".format(i), end=" ")
        print(a_dictionary.get(i))
