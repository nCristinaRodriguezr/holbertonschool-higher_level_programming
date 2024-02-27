#!/usr/bin/python3
"""
A class MyList that inherits from list
"""


class MyList(list):
    """
    Prints the list, but sorted (ascending sort)
    """
    def print_sorted(self):
        ordered_list = sorted(self)
        print(ordered_list)
