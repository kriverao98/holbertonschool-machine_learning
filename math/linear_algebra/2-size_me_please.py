#!/usr/bin/env python3
import numpy as np
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
    new_shape = np.shape(matrix)
    return new_shape
