#!/usr/bin/env python3
"""
Calculate the shape of a matrix.
Returns:
list: A list of integers representing the shape of the matrix.
"""


def matrix_shape(matrix):
    """
    Calculate the shape of a matrix.

    Parameters:
    matrix (list): A list of lists representing the matrix.

    Returns:
    list: A list of integers representing the shape of the matrix.
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0] if matrix else []
    return shape