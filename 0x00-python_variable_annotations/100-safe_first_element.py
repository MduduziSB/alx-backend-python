#!/usr/bin/env python3
"""
Correctly augmentend code with the duck-typed annotations
"""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the Sequence

    Arguments:
    - lst (Sequence)-> Sequence of Any type elements

    Return:

    - Returns the first element of lst
    """
    if lst:
        return lst[0]
    else:
        return None
