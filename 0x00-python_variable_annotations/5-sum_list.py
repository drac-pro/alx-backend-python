#!/usr/bin/env python3
"""defines a type-annotated function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """calculates the sum of element in a list of floats
    Args:
        input_list(list[float]): list of floating point numbers
    Return:
        float: sum of all numbers in the list
    """
    return sum(input_list)
