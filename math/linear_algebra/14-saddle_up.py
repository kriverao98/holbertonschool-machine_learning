#!/usr/bin/env python3
import numpy as np
"""Performs matrix multiplication on two numpy arrays."""


def np_matmul(mat1, mat2):
    """
    Performs matrix multiplication on two numpy arrays.

    Args:
        mat1 (numpy.ndarray): The first matrix.
        mat2 (numpy.ndarray): The second matrix.

    Returns:
        numpy.ndarray: The result of the matrix
        multiplication of mat1 and mat2.
    """
    return np.matmul(mat1, mat2)
