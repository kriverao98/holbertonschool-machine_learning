#!/usr/bin/env python3
"""Concatenates two 2D matrices along a specific axis."""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two 2D matrices along a specific axis.

    Parameters:
    mat1 (list of lists of int/float): The first matrix to concatenate.
    mat2 (list of lists of int/float): The second matrix to concatenate.
    axis (int): The axis along which to concatenate the matrices.
                0 for vertical concatenation, 1 for horizontal concatenation.
                Default is 0.

    Returns:
    list of lists of int/float: The concatenated matrix, or None
    if the matrices cannot be concatenated.
    """
    if not mat1 or not mat2:
        return None

    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return mat1 + mat2
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
    else:
        return None
