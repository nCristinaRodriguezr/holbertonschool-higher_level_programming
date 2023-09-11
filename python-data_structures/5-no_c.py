#!/usr/bin/python3
def no_c(my_string):
    copy_mystring = ""
    for caracter in my_string:
        if caracter != 'C' and caracter != 'c':
            copy_mystring += caracter
    return copy_mystring