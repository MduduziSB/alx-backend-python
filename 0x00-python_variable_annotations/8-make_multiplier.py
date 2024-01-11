#!/usr/bin/env python3
from typing import Callable
"""
Type-annotated function make_multiplier
It takes a float multiplier as argument
and returns a function that multiplies a float by multiplier.
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Calculates the product of the multipier and itself.

    Parameters:
    - multiplier (float): The multiplier value.

    Returns:
    - Callable[[float], float]: multiplier * itself
    """
    def multiplier_function(x: float) -> float:
        """multiplier function"""
        return x * multiplier

    return multiplier_function
