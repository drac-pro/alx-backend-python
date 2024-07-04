#!/usr/bin/env python3
"""defines a type-annotated function element_length"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list of tuples
    Args:
        lst(list[list]): list of list
    Return:
        list[tuple[list, int]]: return a list
    """
    return [(i, len(i)) for i in lst]
