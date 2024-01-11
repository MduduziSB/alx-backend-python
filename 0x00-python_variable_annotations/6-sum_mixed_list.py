#!/usr/bin/env python3
"""
Type-annotated function sum_list
Which takes a list mxd_lst of floats as argument
Returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of floats and integers.

    Parameters:
    - mxd_lst (List[float, int]): The input list of floats and integers.

    Returns:
    - float: The sum of the input list.
    """
    return sum(mxd_lst)
