#!/usr/bin/python3
"""
Matrix Division Module

This module provides a function `matrix_divided(matrix, div)` that divides
all the elements of a matrix
(a list of lists of integers or floats) by a number (div),
and returns a new matrix with
the result rounded to 2 decimal places.

Functions:
    matrix_divided(matrix, div): Divides each element
    of the matrix by the number 'div'.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of list of int/float): A matrix to be divided.
        It must be a list of lists, where each inner list contains
        integers or floats, and all rows must have the same size.
        div (int/float): The divisor by which all elements of
        the matrix will be divided.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If any row in the matrix does not have the same size.
        TypeError: If div is not an integer or float.
        TypeError: If div is zero.

    Returns:
        list of list of float: A new matrix with the
        result of the division, rounded to 2 decimal places.
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix \
                        (list of lists) of integers/floats")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix \
            (list of lists) of integers/floats")

    for row in matrix:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("matrix must be a matrix \
                (list of lists) of integers/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise TypeError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
