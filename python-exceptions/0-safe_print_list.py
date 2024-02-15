#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    element_print = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            element_print = element_print + 1
    except IndexError:
        pass
    finally:
        print()
    return element_print
