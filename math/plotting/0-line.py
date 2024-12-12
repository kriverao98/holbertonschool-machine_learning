#!/usr/bin/env python3
"""
Plots a line graph of y = x^3 for x in the range [0, 10].
"""
import numpy as np
import matplotlib.pyplot as plt


def line():
    """
    Plots a line graph of y = x^3 for x in the range [0, 10].

    The function creates a plot with the y-values being the cube
    of numbers from 0 to 10.
    The plot is displayed with a red line for the y-axis values and the x-axis
    ranging from 0 to 10.
    The figure size is set to 6.4 by 4.8 inches.
    """

    # Generate values and set figures
    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))

    # Y-axis red line
    plt.plot(y, color='red')

    # X-axis ranging from 0 - 10
    plt.xlim(0, 10)

    # Render plot
    plt.show()
