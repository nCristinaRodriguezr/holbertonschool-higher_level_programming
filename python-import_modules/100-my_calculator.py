#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
my_operations = {'+': add, '-': sub, '*': mul, '/': div}
if len(sys.argv)>4 or len(sys.argv)<4:
    print ('Usage: ./100-my_calculator.py <a> <operator> <b>')
    exit(1)
elif sys.argv[2] != '+' and sys.argv[2] != '-' and sys.argv[2] != '*' and sys.argv[2] != '/':
    print('Unknown operator. Available operators: +, -, * and /')
    exit(1)
else:
    result = my_operations[sys.argv[2]](int(sys.argv[1]), int(sys.argv[3]))
    print(f'{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {result}')
    exit(0)
