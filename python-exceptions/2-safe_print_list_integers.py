#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    element_print = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end= "")
            element_print = element_print + 1
        except (ValueError, TypeError):
            pass
    print()
    return element_print
            