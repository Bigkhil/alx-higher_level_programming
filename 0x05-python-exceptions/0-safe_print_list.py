#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cntr = 0
    try:
        for i in range(0, x):
            print(my_list[i], end="")
            cntr += 1
    except IndexError:
        None
    print()
    return cntr
