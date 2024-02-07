#!/usr/bin/python3
for numero in range(122, 96, -1):
    print(chr(numero) if numero % 2 == 0 else chr(numero -32), end='')


