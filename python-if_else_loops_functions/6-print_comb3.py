#!/usr/bin/python3
for numero in range(0, 88):
    if numero / 10 < numero % 10:
        print('{:02}, ' .format(numero), end='')
print(89)
