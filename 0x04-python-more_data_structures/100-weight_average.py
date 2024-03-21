#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        upper = 0
        under = 0
        for i in range(len(my_list)):
            under += my_list[i][1]
            upper += my_list[i][0] * my_list[i][1]
        return (upper / under)
    return 0
