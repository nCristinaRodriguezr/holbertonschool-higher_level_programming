#!/usr/bin/python3
"""
A function that writes a string to a text file (UTF8)
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    This function write to a text file
    """
    with open(filename, 'r+', encoding='utf-8')as archivo:
        contenido = archivo.write(text)
        return contenido
