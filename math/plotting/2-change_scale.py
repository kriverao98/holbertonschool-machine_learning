#!/usr/bin/env python3
"""Plots the exponential decay of Carbon-14 over time with
a logarithmic y-axis scale."""
import numpy as np
import matplotlib.pyplot as plt


def change_scale():
    """
    Plots the exponential decay of Carbon-14 over time with
    a logarithmic y-axis scale.

    The plot includes:
    - A title: "Exponential Decay of C-14"
    - X-axis label: "Time (years)"
    - Y-axis label: "Fraction Remaining"

    The graph is displayed using matplotlib's `plt.show()` function.
    """
    x = np.arange(0, 28651, 5730)
    r = np.log(0.5)
    t = 5730
    y = np.exp((r / t) * x)
    plt.figure(figsize=(6.4, 4.8))

    # x, y plot
    plt.plot(x, y)
    plt.yscale("log")
    plt.xlim(0, 28650)

    # x and y axis labels
    plt.title("Exponential Decay of C-14")
    plt.xlabel("Time (years)")
    plt.ylabel("Fraction Remaining")

    # Graph render
    plt.show()
