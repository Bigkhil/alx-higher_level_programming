#!/usr/bin/python3
# this script gets the peak from an array
def find_peak(list_of_integers):
	'''this fucntion gets a peak from a list of integers'''
	f = 0
	l = len(list_of_integers) - 1

	if len(list_of_integers) == 0:
		return None
	while f <= l:
		if list_of_integers[f] > list_of_integers[f + 1]:
			return list_of_integers[f]
		if list_of_integers[l] > list_of_integers[l - 1]:
			return list_of_integers[l]
		l = l - 1
		f = f + 1
	return list_of_integers[f]
