#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        res = 0
        try:
            res = my_list_1[i] / my_list_2[i]
            new_list.append(res)
        except TypeError:
            print("wrong type")
            new_list.append(0)
            continue
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
            continue
        except IndexError:
            print("out of range")
            new_list.append(0)
            continue
        finally:
            pass
    return new_list
