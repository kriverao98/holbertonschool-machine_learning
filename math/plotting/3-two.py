#!/usr/bin/env python3
"""Plots the exponential decay of two radioactive elements,
Carbon-14 (C-14) and Radium-226 (Ra-226)."""
import numpy as np
import matplotlib.pyplot as plt


def two():
    """
    Plots the exponential decay of two radioactive elements,
    Carbon-14 (C-14) and Radium-226 (Ra-226).

    The plot includes:
    - A dashed red line representing the decay of C-14.
    - A solid green line representing the decay of Ra-226.
    - X-axis labeled as 'Time (years)'.
    - Y-axis labeled as 'Fraction Remaining'.
    - Title 'Exponential Decay of Radioactive Elements'.
    - A legend indicating which line corresponds to which element.

    The x-axis ranges from 0 to 20000 years, and the y-axis ranges from 0 to 1.

    Returns:
        None
    """

    x = np.arange(0, 21000, 1000)
    r = np.log(0.5)
    t1 = 5730
    t2 = 1600
    y1 = np.exp((r / t1) * x)
    y2 = np.exp((r / t2) * x)
    plt.figure(figsize=(6.4, 4.8))

    plt.plot(x, y1, linestyle='dashed', color='red', label='C-14')
    plt.plot(x, y2, color='green', label='Ra-226')

    plt.xlim(0, 20000)
    plt.ylim(0, 1)

    plt.xlabel('Time (years)')
    plt.ylabel('Fraction Remaining')
    plt.title('Exponential Decay of Radioactive Elements')

    plt.legend()
    plt.show()
