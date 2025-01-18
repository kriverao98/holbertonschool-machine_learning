#!/usr/bin/env python3
"""Performs forward propagation for a neural network."""
import tensorflow.compat.v1 as tf

create_layer = __import__('1-create_layer').create_layer


def forward_prop(x, layer_sizes=[], activations=[]):
    """
    Performs forward propagation for a neural network.

    Args:
        x: tf.placeholder, the input data.
        layer_sizes: list of integers, the number of nodes
        in each layer of the network.
        activations: list of activation functions for each layer
        of the network.

    Returns:
        The output of the final layer after forward propagation.
    """
    layer = x
    for size, activation in zip(layer_sizes, activations):
        layer = create_layer(layer, size, activation)
    return layer
