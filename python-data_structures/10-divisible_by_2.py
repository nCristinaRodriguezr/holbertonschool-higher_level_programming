#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for n in my_list:
        mul_2 = my_list[n] % 2
        if mul_2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
