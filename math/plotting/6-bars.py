#!/usr/bin/env python3
"""Generates a bar plot showing the quantity of
different types of fruit per person."""
import numpy as np
import matplotlib.pyplot as plt


def bars():
    """
    Generates a bar plot showing the quantity of
    different types of fruit per person.

    The plot is displayed using matplotlib.

    Returns:
        None
    """
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))
    plt.figure(figsize=(6.4, 4.8))

    labels = ['Farrah', 'Fred', 'Felicia']
    apples = fruit[0]
    bananas = fruit[1]
    oranges = fruit[2]
    peaches = fruit[3]

    bar_width = 0.5

    plt.bar(labels, apples, width=bar_width, color='red', label='apples')
    plt.bar(labels, bananas, width=bar_width, bottom=apples, color='yellow',
            label='bananas')
    plt.bar(labels, oranges, width=bar_width, bottom=apples + bananas,
            color='#ff8000', label='oranges')
    plt.bar(labels, peaches, width=bar_width, bottom=apples +
            bananas + oranges, color='#ffe5b4', label='peaches')

    plt.ylabel('Quantity of Fruit')
    plt.ylim(0, 80)
    plt.yticks(np.arange(0, 81, 10))
    plt.title('Number of Fruit per Person')
    plt.legend()

    plt.show()
