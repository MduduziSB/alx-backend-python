#!/usr/bin/env python3
"""
type-annotated function floor
which takes a float n as argument
and returns the floor of the float
"""


def floor(n: float) -> int:
    """
    Returns the floor of the given float.
    Parameters:
    - n (float): The input float.
    Returns:
    - int: The floor of the input float.
    """
    return int(n) // 1
