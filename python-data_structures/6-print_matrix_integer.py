#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0])>0:
        for fila in matrix:
            for i in range(len(fila)):
                if i == len(fila)-1:
                    print(f'{fila[i]}')
                else:
                    print(f'{fila[i]}', end = " ")
    else:
        print('')
