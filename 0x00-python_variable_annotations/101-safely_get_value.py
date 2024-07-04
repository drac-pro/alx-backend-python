#!/usr/bin/env python3
"""defines a type-annotated function safely_get_value"""
from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """returns the value of a key in a dictionary otherwise returns default"""
    if key in dct:
        return dct[key]
    else:
        return default
