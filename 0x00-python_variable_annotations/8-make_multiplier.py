#!/usr/bin/env python3
"""defines a type-annotated function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a multiplier function
    Args:
        multiplier(float): floating point number
    Return:
        function: a funtion that multiplies the multiplier by another number
    """
    return lambda x: x * multiplier
