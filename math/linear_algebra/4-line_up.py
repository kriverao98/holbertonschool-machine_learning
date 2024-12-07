#!/usr/bin/env python3
"""Adds two arrays element-wise."""


def add_arrays(arr1, arr2):
    """
    Adds two arrays element-wise.

    Args:
        arr1 (list): The first array.
        arr2 (list): The second array.

    Returns:
        list: A new array containing the element-wise sums of arr1 and arr2.
              If the arrays are not of the same length, returns None.
    """
    res = []
    for a, b in zip((arr1), (arr2)):
        if len(arr1) == len(arr2):
            return list(map(sum, zip(arr1, arr2)))
        else:
            return None
