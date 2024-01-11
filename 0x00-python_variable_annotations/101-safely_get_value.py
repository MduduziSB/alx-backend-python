#!/usr/bin/env python3
"""
Adds type annotations to the function,
Given the parameters and the return values
"""
from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Safely gets the value from a dictionary based on the key.
    If the key is present, returns the corresponding value.
    If the key is not present, returns the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
