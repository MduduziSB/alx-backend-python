#!/usr/bin/env python3
"""
Type-annotated function make_multiplier
It takes a float multiplier as argument
and returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Calculates the product of the multipier and itself.

    Parameters:
    - multiplier (float): The multiplier value.

    Returns:
    - Callable[[float], float]: multiplier * itself
    """
    return lambda x: x * multiplier
