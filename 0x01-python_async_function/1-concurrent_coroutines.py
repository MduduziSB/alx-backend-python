#!/usr/bin/env python3
"""
Imports wait_random from 0-basic_async_syntax.py file
Defines an async routine called wait_n
- takes in 2 int arguments (in this order): n and max_delay.
Spawns wait_random n times with the specified max_delay.

wait_n returns the list of all the delays (float values).
The list of the delays is arranged in ascending order without using sort().
"""
import asyncio, time, random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    This coroutine spawns wait_random coroutine n times.
    Aurguments:
    - n (int) int the number of times wait_random should be spawned
    - max_delay (int) int the maximum delay in seconds

    Return:
    - List of delays in seconds (float)
    """
    delay_list = []

    for count in range (0, n):
        delay = await wait_random(max_delay)
        delay_list.append(delay)
    return sorted(delay_list)
