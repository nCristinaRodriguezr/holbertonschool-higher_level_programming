#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbers = set()
    suma = 0
    for num in my_list:
        if isinstance(num, int) and num not in unique_numbers:
            suma += num
            unique_numbers.add(num)
    return suma
