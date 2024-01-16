#!/usr/bin/env python3
"""
This module imports async_comprehension from 1-async_comprehension.py file,
it then defines a measure_runtime coroutine that executes async_comprehension
four times in parallel using asyncio.gather.

measure_runtime measures the total runtime and return it.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total time that this coroutine takes to complete execution
    """
    start_time = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.perf_counter()
    return end_time - start_time
