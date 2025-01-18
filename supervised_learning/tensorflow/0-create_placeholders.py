#!/usr/bin/env python3
"""Returns two placeholders, x and y, for the neural network."""
import tensorflow.compat.v1 as tf


def create_placeholders(nx, classes):
    """
    Returns two placeholders, x and y, for the neural network.

    Args:
    nx: int, the number of feature columns in our data
    classes: int, the number of classes in our classifier

    Returns:
    x: tf.placeholder, placeholder for the input data
    y: tf.placeholder, placeholder for the one-hot labels
    """
    x = tf.placeholder(tf.float32, shape=[None, nx], name='x')
    y = tf.placeholder(tf.float32, shape=[None, classes], name='y')
    return x, y
