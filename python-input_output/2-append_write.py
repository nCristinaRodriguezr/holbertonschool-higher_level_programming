#!/usr/bin/python3
"""
A function that appends a string at the end of a text file (UTF8)
and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """
    This function add a string at the end
    """
    with open(filename, 'a', encoding="utf-8") as archivo:
        contenido = archivo.write(text)
        return contenido
