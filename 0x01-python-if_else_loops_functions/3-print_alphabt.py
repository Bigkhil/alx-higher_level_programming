#!/usr/bin/python3
itr = 97
while itr <= 122:
    if chr(itr) == 'q' or chr(itr) == 'e':
        itr += 1
        continue
    print("{}".format(chr(itr)), end="")
    itr += 1
