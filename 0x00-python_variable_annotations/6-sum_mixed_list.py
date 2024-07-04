#!/usr/bin/env python3
"""defines a type-annotated function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum all numbers in a list of integers and floats
    Args:
        mxd_lst(list[int | float]): list of ints or floats
    Return:
        float: sum of all the numbers
    """
    return sum(mxd_lst)
