#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    mx = max(len(my_list_1, my_list_2))
    new_list = []
    for i in range(0, mx):
        res = 0
        try:
            res = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            print("wrong type")
            res = 0
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        new_list.append(res)
    return new_list
        
        
