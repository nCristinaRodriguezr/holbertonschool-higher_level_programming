#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_square = []
    for fila in matrix:
        result = []
        for columna in fila:
            operation = columna ** 2
            result.append(operation)
        matrix_square.append(result)
    return matrix_square
