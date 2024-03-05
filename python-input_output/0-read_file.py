#!/usr/bin/python3
"""
A function that reads a text file (UTF8) and prints it to stdout.
"""


def read_file(filename=""):
    """
    This function read a file.
    """
    with open(filename, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
        print(contenido)
