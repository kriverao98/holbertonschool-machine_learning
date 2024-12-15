#!/usr/bin/env python3
"""Calculate the summation of squares of
integers from 1 to n."""


def summation_i_squared(n):
    """
    Calculate the summation of squares of integers from 1 to n.

    Parameters:
    n (int): The upper limit of the summation.
    Must be a positive integer.

    Returns:
    int: The summation of squares of integers from 1 to n,
    or None if n is not a positive integer.
    """
    if not isinstance(n, int) or n < 1:
        return None
    return n * (n + 1) * (2 * n + 1) // 6
