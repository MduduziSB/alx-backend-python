#!/usr/bin/env python3
from typing import Iterable, List, Sequence, Tuple
"""
Annotate the below function’s parameters
and return values with the appropriate types
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Computes the length of each element in the input iterable.

    Parameters:
    - lst (Iterable[Sequence]): The input iterable containing sequences.

    Returns:
    - List[Tuple[Sequence, int]]: A list of tuples where each tuple
    -- Contains a sequence from the input and its length.
    """
    return [(i, len(i)) for i in lst]
