#!/usr/bin/env python3
"""
    Optimization project
"""
import tensorflow as tf


def create_batch_norm_layer(prev, n, activation):
    """ Creates a batch normalization layer
        prev is activated output of previous layer
        n is number of nodes
        activation is activation function to be used

        kernal initializer
        tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
        gamma and beta initialized as vectors of 1, 0 respectively
        epsilon of 1e-8

        Returns: normlized Z matrix
    """
    init = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    x = tf.layers.Dense(units=n, activation=None, kernel_initializer=init)
    x_prev = x(prev)
    scale = tf.Variable(tf.constant(1.0, shape=[n]), name='gamma')
    mean, variance = tf.nn.moments(x_prev, axes=[0])
    offset = tf.Variable(tf.constant(0.0, shape=[n]), name='beta')
    variance_epsilon = 1e-8

    normalization = tf.nn.batch_normalization(
        x_prev,
        mean,
        variance,
        offset,
        scale,
        variance_epsilon,
    )
    return activation(normalization)
