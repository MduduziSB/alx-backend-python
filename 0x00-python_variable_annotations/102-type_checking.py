#!/usr/bin/env python3
"""
Validated piece of code using mypy
"""
from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Returns a tuple

    Elements:
    - integer elements

    Function arguments:
    - lst (Tuple)
    - factor (int)
    """
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
