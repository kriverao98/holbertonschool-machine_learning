#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt


def all_in_one():

    y0 = np.arange(0, 11) ** 3

    mean = [69, 0]
    cov = [[15, 8], [8, 15]]
    np.random.seed(5)
    x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
    y1 += 180

    x2 = np.arange(0, 28651, 5730)
    r2 = np.log(0.5)
    t2 = 5730
    y2 = np.exp((r2 / t2) * x2)

    x3 = np.arange(0, 21000, 1000)
    r3 = np.log(0.5)
    t31 = 5730
    t32 = 1600
    y31 = np.exp((r3 / t31) * x3)
    y32 = np.exp((r3 / t32) * x3)

    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)

    fig = plt.figure(figsize=(10, 8))
    fig.suptitle('All in One', fontsize='x-small')

    # First subplot
    ax1 = fig.add_subplot(3, 2, 1)
    ax1.plot(np.arange(0, 11), y0, color='r')
    ax1.set_title('y = x^3', fontsize='x-small')

    # Second subplot
    ax2 = fig.add_subplot(3, 2, 2)
    ax2.scatter(x1, y1, color='m', s=10)
    ax2.set_title('Men\'s Height vs Weight', fontsize='x-small')

    # Third subplot
    ax3 = fig.add_subplot(3, 2, 3)
    ax3.plot(x2, y2)
    ax3.set_yscale('log')
    ax3.set_title('Exponential Decay of C-14', fontsize='x-small')

    # Fourth subplot
    ax4 = fig.add_subplot(3, 2, 4)
    ax4.plot(x3, y31, 'r--', label='C-14')
    ax4.plot(x3, y32, 'g-', label='Ra-226')
    ax4.legend(fontsize='x-small')
    ax4.set_title('Exponential Decay of Radioactive Elements',
                  fontsize='x-small')

    # Fifth subplot
    ax5 = fig.add_subplot(3, 2, (5, 6))
    ax5.hist(student_grades, bins=10, edgecolor='black')
    ax5.set_title('Project A', fontsize='x-small')

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()
