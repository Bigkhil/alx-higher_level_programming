#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in matrix[i]:
            print("{:d}".format(int(matrix[i][j])), end=" ")
        print("\n")
