#!/usr/bin/env python3
"""Calculate the derivative of a polynomial."""


def poly_derivative(poly):
    """
    Calculate the derivative of a polynomial.
    Args:
        poly (list): A list of coefficients representing a polynomial.
        The index of each element represents the power of x
        that the coefficient multiplies.
    Returns:
        list: A list of coefficients representing the derivative of
        the polynomial. If the input is invalid (not a list,
        empty list, or contains non-numeric elements), returns None.
        If the polynomial is a constant, returns [0].
    """
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    if not all(isinstance(x, (int, float)) for x in poly):
        return None

    if len(poly) == 1:
        return [0]

    derivative = [i * poly[i] for i in range(1, len(poly))]

    return derivative
