#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()): 
    if len(tuple_a) == 0:
        copy_tuple_a = (0, 0)
    elif len(tuple_a) == 1:
        copy_tuple_a = tuple_a + (0,)
    else:
        copy_tuple_a = tuple_a

    if len(tuple_b) == 0:
        copy_tuple_b = (0, 0)
    elif len(tuple_b) == 1:
        copy_tuple_b = tuple_b + (0,)
    else:
        copy_tuple_b = tuple_b
   
    suma_tuples = (copy_tuple_a[0] + copy_tuple_b[0], copy_tuple_a[1] + copy_tuple_b[1])
    return suma_tuples