#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = []
    if a_dictionary:
        for key, valor in a_dictionary.items():
            if valor == value:
                keys.append(key)
        if len(keys) > 0:
            for key in keys:
                del a_dictionary[key]
    return a_dictionary