#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in matrix:
            if len(matrix) == 1 and len(matrix[0]) == 0:
                print("")
                continue
            for j in i:
                print("{:d}".format(j), end=" " if j != i[-1] else "\n")
