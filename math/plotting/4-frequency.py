#!/usr/bin/env python36556
"""Generates a histogram of student grades."""
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """
    Generates a histogram of student grades.

    The histogram has the following properties:
    - Title: 'Project A'
    - X-axis label: 'Grades'
    - Y-axis label: 'Number of Students'
    - Bins: Ranges from 0 to 100 with a step of 10
    - X-axis limit: 0 to 100
    - Y-axis limit: 0 to 30
    """

    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    plt.title('Project A')
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')

    bins = range(0, 101, 10)

    plt.hist(student_grades, bins=bins, edgecolor='black')
    plt.xlim(0, 100)
    plt.ylim(0, 30)

    plt.show()
