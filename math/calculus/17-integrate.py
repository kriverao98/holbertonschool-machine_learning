#!/usr/bin/env python3
"""Calculate the integral of a polynomial."""


def poly_integral(poly, C=0):
    """
    Calculate the integral of a polynomial.

    Args:
        poly (list): A list of coefficients representing a polynomial.
                     The index of each element represents the power of x.
                     For example, [5, 3, 0, 1] represents 5 + 3x + x^3.
        C (int, float): The constant of integration. Defaults to 0.

    Returns:
        list: A list of coefficients representing the integral
        of the polynomial.
        If the input is invalid, returns None.
    """
    if not isinstance(poly, list) or not isinstance(C, (int, float)):
        return None
    if not all(isinstance(coef, (int, float)) for coef in poly):
        return None

    integral = [C]
    for i in range(len(poly)):
        coef = poly[i] / (i + 1)
        if coef.is_integer():
            coef = int(coef)
        integral.append(coef)

    return integral
