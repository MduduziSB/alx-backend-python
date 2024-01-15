#!/usr/bin/env python3
"""
This is an asynchronous coroutine.
It takes in an integer argument -
- (max_delay, with a default value of 10) named wait_random
wait-random waits for a random delay between 0 and max_delay
seconds and eventually returns it.

Uses the random module.
"""
import asyncio
import time
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    A coroutine that awaits random time and finnally returns it
    parameter(s):
    - max_delay: integer number

    Return:
    - Delayed time: floating point number in seconds
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
