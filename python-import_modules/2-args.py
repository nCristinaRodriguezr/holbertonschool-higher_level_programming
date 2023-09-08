#!/usr/bin/python3
import sys
i = 0
if len(sys.argv)==1:
    print('0 arguments.')
elif len(sys.argv)==2:
    print('1 argument:') 
else:
    print(f'{len(sys.argv)-1}: arguments')
for i in range(1, len(sys.argv)):
    print(f'{i}: {sys.argv[i]}')


