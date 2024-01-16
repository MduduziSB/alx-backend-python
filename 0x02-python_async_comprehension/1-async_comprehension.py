#!/usr/bin/env python3
"""
This module imports async_generator from the 0-async_generator.py,
then write a coroutine called async_comprehension that takes no arguments.

The coroutine collects 10 random numbers,
it does that using an async comprehensing over async_generator,
then return the 10 random numbers.
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Computes a list comprehension of 10 randomly generated numbers

    Arguments:
    - No arguments

    Return:
    list of floating point numbers
    """
    rand_numbers = [item async for item in async_generator()]
    return rand_numbers
