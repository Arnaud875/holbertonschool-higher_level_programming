#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_ = []

    for i in matrix:
        arr = []
        for j in i:
            arr.append(j * j)
        matrix_.append(arr)
    return matrix_
