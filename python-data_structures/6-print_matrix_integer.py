#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
    else:
        for i in matrix:
            length = len(i)
            for idx, j in enumerate(i):
                if idx + 1 != length:
                    print("{:d}".format(j), end=" ")
                else:
                    print("{:d}".format(j))
