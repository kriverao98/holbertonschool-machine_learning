#!/usr/bin/env python3
import numpy as np
"""Concatenates two numpy arrays along a specified axis."""


def np_cat(mat1, mat2, axis=0):
    """
    Concatenates two numpy arrays along a specified axis.

    Parameters:
    mat1 (numpy.ndarray): The first array to concatenate.
    mat2 (numpy.ndarray): The second array to concatenate.
    axis (int, optional): The axis along which the arrays will be
    concatenated. Default is 0.

    Returns:
    numpy.ndarray: The concatenated array.
    """
    return np.concatenate((mat1, mat2), axis=axis)
