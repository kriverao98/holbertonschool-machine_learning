#!/usr/bin/env python3
"""Shuffles the data points in two matrices the same way."""
import numpy as np


def shuffle_data(X, Y):
    """Shuffles the data points in two matrices the same way.

    Args:
        X (numpy.ndarray): The first matrix of shape (m, nx) to shuffle.
        Y (numpy.ndarray): The second matrix of shape (m, ny) to shuffle.

    Returns:
        tuple: The shuffled X and Y matrices.
    """
    assert X.shape[0] == Y.shape[0]
    permutation = np.random.permutation(X.shape[0])
    return X[permutation], Y[permutation]
