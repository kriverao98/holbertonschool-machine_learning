#!/usr/bin/env python3
"""Script to optimize DNN using Adam with Tensorflow"""

import tensorflow as tf


def create_Adam_op(alpha, beta1, beta2, epsilon):
    """
    Function to set up the Adam optimization algorithm in TensorFlow
    Args:
        alpha: learning rate
        beta1: weight used for the first moment
        beta2: weight used for the second moment
        epsilon: small number to avoid division by zero

    Returns: Adam optimizer
    """
    optimizer = tf.train.AdamOptimizer(learning_rate=alpha,
                                       beta1=beta1,
                                       beta2=beta2,
                                       epsilon=epsilon)
    return optimizer
