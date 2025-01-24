#!/usr/bin/env python3
"""Creates mini-batches from the input data."""
import numpy as np
shuffle_data = __import__('2-shuffle_data').shuffle_data


def create_mini_batches(X, Y, batch_size):
    """
    Creates mini-batches from the input data.
    Args:
        X (numpy.ndarray): The input data of shape (m, n)
        where m is the number of examples and n is the number of features.
        Y (numpy.ndarray): The labels of shape (m, k) where m is
        the number of examples and k is the number of classes.
        batch_size (int): The size of each mini-batch.
    Returns:
        list of tuples: A list of mini-batches, where
        each mini-batch is a tuple (X_batch, Y_batch).
    """
    m = X.shape[0]
    X, Y = shuffle_data(X, Y)

    mini_batches = []
    num_complete_batches = m // batch_size

    for k in range(num_complete_batches):
        X_batch = X[k * batch_size:(k + 1) * batch_size]
        Y_batch = Y[k * batch_size:(k + 1) * batch_size]
        mini_batches.append((X_batch, Y_batch))

    if m % batch_size != 0:
        X_batch = X[num_complete_batches * batch_size:]
        Y_batch = Y[num_complete_batches * batch_size:]
        mini_batches.append((X_batch, Y_batch))

    return mini_batches
