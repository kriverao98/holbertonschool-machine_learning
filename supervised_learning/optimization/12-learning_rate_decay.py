#!/usr/bin/env python3
"""
    Optimization project
"""
import tensorflow as tf


def learning_rate_decay(alpha, decay_rate, decay_step):
    """ creates learning rate decay operation in tensorflow
        using inverse time decay

        alpha is the original learning rate
        decay_rate is the weight used to determine the rate at which alpha will decay
        decay_step is the number of passes of gradient descent that should occur before alpha is decayed further

        Returns: the learning rate decay operation
    """
    global_step = tf.Variable(0, trainable=False, name='global_step')
    learning_rate = tf.compat.v1.train.inverse_time_decay(alpha, global_step, decay_step,
                                                          decay_rate, staircase=True)
    return learning_rate
