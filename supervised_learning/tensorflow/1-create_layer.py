import tensorflow as tf
"""Creates a dense layer for a neural network using TensorFlow."""


def create_layer(prev, n, activation):
    """
    Creates a dense layer for a neural network using TensorFlow.

    Args:
        prev (tf.Tensor): The output tensor from the previous layer.
        n (int): The number of units (neurons) in the dense layer.
        activation (callable): The activation function to use in the layer.

    Returns:
        tf.Tensor: The output tensor of the created dense layer.
    """
    initializer = tf.keras.initializers.VarianceScaling(mode='fan_avg')
    layer = tf.keras.layers.Dense(units=n, activation=activation,
                                  kernel_initializer=initializer, name='layer')
    return layer(prev)
