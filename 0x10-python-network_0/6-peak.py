#!/usr/bin/python3
'''this script gets the peak from an array'''


def find_peak(list_of_integers):
    '''this fucntion gets a peak from a list of integers'''
    first = 0
    last = len(list_of_integers) - 1

    if len(list_of_integers) == 0:
        return None
    while first <= last:
        if list_of_integers[first] > list_of_integers[first + 1]:
            return list_of_integers[first]
        if list_of_integers[last] > list_of_integers[last - 1]:
            return list_of_integers[last]
        last = last - 1
        first = first + 1
    return list_of_integers[first]
