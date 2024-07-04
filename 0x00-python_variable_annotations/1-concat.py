#!/usr/bin/env python3
"""defines a type-annotated function concat"""


def concat(str1: str, str2: str) -> str:
    """concatenates two strings
    Args:
        str1(str): string one
        str2(str): string two

    Return:
        str: the resulting string
    """
    return str1 + str2
