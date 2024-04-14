#!/usr/bin/python3
'''matrix divided module'''


def matrix_divided(matrix, div):
    '''matrix divided function'''
    if isinstance(matrix, list):
        for i in range(len(matrix)):
            if not isinstance(matrix[i], list):
                raise TypeError(
                    "matrix must be a matrix \
                        (list of lists) of integers/floats")
            elif len(matrix[i] != matrix[0]):
                raise TypeError(
                    "Each row of the matrix must have the same size")
            else:
                if not all(isinstance(num, (int, float)) for num in matrix[i]):
                    raise TypeError(
                        "matrix must be a matrix \
                            (list of lists) of integers/floats")
    else:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        for j in range(matrix[i]):
            matrix[i][j] = matrix[i][j] / div
            matrix[i][j] = round(matrix[i][j], 2)
    return matrix
