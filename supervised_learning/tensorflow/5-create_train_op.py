#!/usr/bin/env python3
"""Creates the training operation for the network."""
import tensorflow.compat.v1 as tf


def create_train_op(loss, alpha):
    """
    Creates the training operation for the network.

    Parameters:
    loss (tf.Tensor): The loss of the network's prediction.
    alpha (float): The learning rate.

    Returns:
    tf.Operation: An operation that trains the network using gradient descent.
    """
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=alpha)
    train_op = optimizer.minimize(loss)
    return train_op
