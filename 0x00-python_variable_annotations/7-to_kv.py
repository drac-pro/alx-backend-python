#!/usr/bin/env python3
"""defines a type-annotated function to_kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple
    Args:
        k(str): a string
        v(int | float): an integer or float number
    Return:
        tuple[str, int | float]: the tuple
    """
    return (k, v**2)
