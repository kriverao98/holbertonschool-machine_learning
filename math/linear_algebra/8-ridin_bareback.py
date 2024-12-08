#!/usr/bin/env python3
"""Multiplies two matrices and returns the result."""


def mat_mul(mat1, mat2):
    """
    Multiplies two matrices and returns the result.

    Args:
        mat1 (list of list of int/float): The first matrix to be multiplied.
        mat2 (list of list of int/float): The second matrix to be multiplied.

    Returns:
        list of list of int/float: The resulting matrix
        product of mat1 and mat2.
    """
    if len(mat1[0]) != len(mat2):
        return None
    result = []
    for i in range(0, len(mat1)):
        temp = []
        for j in range(0, len(mat2[0])):
            s = 0
            for k in range(0, len(mat1[0])):
                s += mat1[i][k] * mat2[k][j]
            temp.append(s)
        result.append(temp)

    return result
