#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    order = sorted(my_list)
    maximo = order[-1]
    return maximo
