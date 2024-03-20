#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = matrix[:]
    for i in new:
        for j in i:
            j = j ** 2
    return new
