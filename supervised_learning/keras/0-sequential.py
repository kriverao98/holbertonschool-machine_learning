#!/usr/bin/env python3
""" Builds a neural network model using Keras."""
import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """
    Builds a neural network model using Keras.
    Args:
        nx (int): The number of input features to the network.
        layers (list of int): A list containing the
        number of nodes in each layer of the network.
        activations (list of str): A list containing
        the activation functions used for each layer of the network.
        lambtha (float): The L2 regularization parameter.
        keep_prob (float): The probability that a node
        will be kept during dropout.
    Returns:
        keras.Model: The constructed Keras model.
    """
    model = K.Sequential()
    L2 = K.regularizers.l2(lambtha)
    for i in range(len(layers)):
        if i == 0:
            model.add(K.layers.Dense(
                layers[i], input_shape=(nx,),
                activation=activations[i],
                kernel_regularizer=L2,
                name='dense'))
        else:
            model.add(K.layers.Dropout(1 - keep_prob))
            model.add(K.layers.Dense(
                layers[i], activation=activations[i],
                kernel_regularizer=L2,
                name='dense_' + str(i)))
    return model
