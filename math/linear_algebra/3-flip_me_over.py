#!/usr/bin/env python3
"""
Transposes a given 2D matrix.
"""


def matrix_transpose(matrix):
    """
    Transposes a given 2D matrix.

    Args:
        matrix (list of list of int/float): The matrix to be transposed.

    Returns:
        list of list of int/float: The transposed matrix.
    """
    return [[matrix[j][i] for j in range(len(matrix))]
            for i in range(len(matrix[0]))]
