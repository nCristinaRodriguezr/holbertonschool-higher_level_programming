#!/usr/bin/python3
import sys
from add_0 import add
if __name__ == "__main__":
    result = 0
    if len(sys.argv) == 1:
        print('0')
    else:
        for i in range(1, len(sys.argv)):
            numero = int(sys.argv[i])
            result = add(result, numero)
        print('{}'.format(result))
