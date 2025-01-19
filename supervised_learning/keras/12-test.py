"""Tests a neural network."""
import tensorflow.keras as K


def test_model(network, data, labels, verbose=True):
    """
    Tests a neural network.

    Parameters:
    - network: the network model to test
    - data: the input data to test the model with
    - labels: the correct one-hot labels of data
    - verbose: boolean that determines if output should
    be printed during the testing process

    Returns:
    - loss: the loss of the model with the testing data
    - accuracy: the accuracy of the model with the testing data
    """
    loss, accuracy = network.evaluate(data, labels, verbose=verbose)
    return loss, accuracy
