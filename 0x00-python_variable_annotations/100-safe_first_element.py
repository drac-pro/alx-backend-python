#!/usr/bin/env python3
"""defines duck-typed annotated function safe_first_element"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns first element of a list or none if not a list
    Args:
        lst(list[any] | None): can be a list
    Return:
        any | None:
    """
    if lst:
        return lst[0]
    else:
        return None
