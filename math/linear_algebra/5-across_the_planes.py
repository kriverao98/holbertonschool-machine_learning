#!/usr/bin/env python3
"""Adds two 2D matrices element-wise."""


def add_matrices2D(mat1, mat2):
    """
    Adds two 2D matrices element-wise.
    Args:
        mat1 (list of list of int/float): The first 2D matrix.
        mat2 (list of list of int/float): The second 2D matrix.
    Returns:
        list of list of int/float: A new 2D matrix containing
        the element-wise sums.
        None: If the matrices are not the same size or contain
        non-numeric elements.
    """
    if (not mat1 or not mat2 or len(mat1) != len(mat2) or
            len(mat1[0]) != len(mat2[0])):
        return None

    result = []
    for row in range(len(mat1)):
        result_row = []
        for col in range(len(mat1[0])):
            if isinstance(mat1[row][col], (int, float)) and isinstance(
                mat2[row][col], (int, float)
            ):
                result_row.append(mat1[row][col] + mat2[row][col])
            else:
                return None
        result.append(result_row)

    return result
