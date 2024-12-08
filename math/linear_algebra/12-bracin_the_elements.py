#!/usr/bin/env python3
"""Perform element-wise addition, subtraction, multiplication,
    and division on two matrices.
"""


def np_elementwise(mat1, mat2):
    """
    Perform element-wise addition, subtraction, multiplication,
    and division on two matrices.

    Args:
        mat1 (numpy.ndarray): The first input matrix.
        mat2 (numpy.ndarray): The second input matrix.

    Returns:
        tuple: A tuple containing four numpy.ndarrays:
            - The element-wise sum of mat1 and mat2.
            - The element-wise difference of mat1 and mat2.
            - The element-wise product of mat1 and mat2.
            - The element-wise quotient of mat1 and mat2.
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
