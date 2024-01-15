#!/usr/bin/env python3
"""
Imports wait_n into 2-measure_runtime.py.

Creates a measure_time function with integers n and max_delay as arguments
It then measures the total execution time for wait_n(n, max_delay),
and returns total_time / n.
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: float):
    """
    This function computes the amount of time wait_n needed to complete
    Arguments:
    - n (int) this is the number of times wait_n spawns
    - max_delay (int) this is the maximum amount time wait_random delays/sleeps

    Return:
    This function returns the total amount of time wait_n takes per n
    """
    s = time.perf_counter()

    asyncio.run(wait_n(n, max_delay))

    return (time.perf_counter() - s) / n
