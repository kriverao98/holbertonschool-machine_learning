#!/usr/bin/env python3
"""Calculates the exponentially weighted moving average of a data set."""


def moving_average(data, beta):
    """
    Calculates the exponentially weighted moving average of a data set.

    Args:
        data (list or numpy.ndarray): The list or array of data points to
        calculate the moving average for.
        beta (float): The weight used for the moving average calculation.
        Should be between 0 and 1.

    Returns:
        list: A list containing the exponentially weighted moving
        averages of the data points.
    """
    moving_averages = []
    v = 0
    for t in range(len(data)):
        v = beta * v + (1 - beta) * data[t]
        bias_correction = 1 - beta ** (t + 1)
        moving_averages.append(v / bias_correction)
    return moving_averages
