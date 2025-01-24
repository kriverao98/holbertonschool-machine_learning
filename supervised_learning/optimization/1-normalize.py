#!/usr/bin/env python3
"""Normalizes (standardizes) a matrix."""
import numpy as np


def normalize(X, m, s):
    """
    Normalizes (standardizes) a matrix.

    Parameters:
    X (numpy.ndarray): The matrix to normalize of shape (d, nx)
    m (numpy.ndarray): The mean of all features of X of shape (nx,)
    s (numpy.ndarray): The standard deviation of all features of X
    of shape (nx,)

    Returns:
    numpy.ndarray: The normalized X matrix
    """
    return (X - m) / s
