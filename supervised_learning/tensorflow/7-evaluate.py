#!/usr/bin/env python3
"""
Evaluates a trained model and makes
predictions on the given data.
"""
import tensorflow.compat.v1 as tf
import numpy as np


def evaluate(X, Y, save_path):
    """
    Evaluates a trained model and makes predictions on the given data.
    Args:
        X (numpy.ndarray): Input data to evaluate the model on.
        Y (numpy.ndarray): True labels corresponding to the input data.
        save_path (str): Path where the trained model is saved.
    Returns:
        tuple: A tuple containing:
            - predictions (numpy.ndarray):
            The predicted values for the input data.
            - accuracy (float): The accuracy of the model on the given data.
            - loss (float): The loss of the model on the given data.
    """
    # Load the model
    model = tf.keras.models.load_model(save_path)

    # Evaluate the model
    loss, accuracy = model.evaluate(X, Y, verbose=0)

    # Make predictions
    predictions = model.predict(X)

    return predictions, accuracy, loss
