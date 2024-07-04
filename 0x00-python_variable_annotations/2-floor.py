#!/usr/bin/env python3
"""defines a type-annotated function floor"""
import math


def floor(n: float) -> int:
    """returns the floor of a floating point number
    Args:
        n(float): floating point number
    Return:
        int: floor of the float number
    """
    return math.floor(n)
