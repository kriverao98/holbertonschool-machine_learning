#!/usr/bin/env python3
"""Trains a neural network using TensorFlow and saves the model.
"""
import tensorflow.compat.v1 as tf


def train(X_train, Y_train, X_valid, Y_valid, layer_sizes,
          activations, alpha, iterations, save_path="/tmp/model.ckpt"):
    """
    Trains a neural network using TensorFlow and saves the model.

    Args:
        X_train (numpy.ndarray): Training data input features.
        Y_train (numpy.ndarray): Training data labels.
        X_valid (numpy.ndarray): Validation data input features.
        Y_valid (numpy.ndarray): Validation data labels.
        layer_sizes (list): List containing the number of
        nodes in each layer of the network.
        activations (list): List containing the activation
        functions for each layer of the network.
        alpha (float): Learning rate.
        iterations (int): Number of iterations to train the model.
        save_path (str): Path where the trained model will be saved.

    Returns:
        str: Path where the trained model is saved.
    """
    x, y = create_placeholders(X_train.shape[1], Y_train.shape[1])
    y_pred = forward_prop(x, layer_sizes, activations)
    loss = calculate_loss(y, y_pred)
    accuracy = calculate_accuracy(y, y_pred)
    train_op = create_train_op(loss, alpha)

    tf.add_to_collection('x', x)
    tf.add_to_collection('y', y)
    tf.add_to_collection('y_pred', y_pred)
    tf.add_to_collection('loss', loss)
    tf.add_to_collection('accuracy', accuracy)
    tf.add_to_collection('train_op', train_op)

    init = tf.global_variables_initializer()
    saver = tf.train.Saver()

    with tf.Session() as sess:
        sess.run(init)
        for i in range(iterations + 1):
            if i % 100 == 0 or i == iterations:
                train_cost, train_accuracy = sess.run(
                    [loss, accuracy], feed_dict={x: X_train, y: Y_train}
                )
                valid_cost, valid_accuracy = sess.run(
                    [loss, accuracy], feed_dict={x: X_valid, y: Y_valid}
                )
                print(f"After {i} iterations:")
                print(f"\tTraining Cost: {train_cost}")
                print(f"\tTraining Accuracy: {train_accuracy}")
                print(f"\tValidation Cost: {valid_cost}")
                print(f"\tValidation Accuracy: {valid_accuracy}")
            if i < iterations:
                sess.run(train_op, feed_dict={x: X_train, y: Y_train})

        save_path = saver.save(sess, save_path)
    return save_path
