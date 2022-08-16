# Enter you module contents here
"""Provides methods to calculate the area and hypotenuse of a right-angled triangle"""
from math import sqrt

__version__ = "1"
__author__ = "miette"

def hypothenuse(a, b):
    """Calculates and returns the hypotenuse of a right-angled triangle"""
    c = sqrt(a**2 + b**2)
    return c

def area(b, h):
    """Calculates and returns the area of a right-angled triangle"""
    area = (b * h)/2
    return area