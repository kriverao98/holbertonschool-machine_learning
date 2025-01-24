#!/usr/bin/env python3
import numpy as np
"""Calculates the normalization (standardization) constants of a matrix."""


def normalization_constants(X):
    """
    Calculates the normalization (standardization) constants of a matrix.

    Parameters:
    X (numpy.ndarray): The matrix of shape (m, nx) to normalize
        - m is the number of data points
        - nx is the number of features

    Returns:
    tuple: The mean and standard deviation of each feature, respectively
    """
    mean = np.mean(X, axis=0)
    std_dev = np.std(X, axis=0)
    return mean, std_dev
