#!/usr/bin/env python3
"""
This is type-annotated function to_kv
- It takes a string k and an int OR float v as arguments
- It then returns a tuple.
- The first element of the tuple is the string k.
- The second element is the square of the int/float v (float annotated).
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple

    Elements:
    - k (str)
    - v ** 2 (float)
    """
    return (k, v ** 2)
