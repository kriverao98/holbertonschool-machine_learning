#!/usr/bin/env python3
"""Sets up the gradient descent with momentum optimization
algorithm in TensorFlow."""
import tensorflow as tf


def create_momentum_op(alpha, beta1):
    """
    Sets up the gradient descent with momentum optimization
    algorithm in TensorFlow.

    Parameters:
    alpha (float): The learning rate.
    beta1 (float): The momentum weight.

    Returns:
    optimizer: The momentum optimizer operation.
    """
    optimizer = tf.train.MomentumOptimizer(learning_rate=alpha, momentum=beta1)
    return optimizer
