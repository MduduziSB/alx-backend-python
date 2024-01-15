#!/usr/bin/env python3
"""
Implementation of task_0 using regular function syntax.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Arguments:
    - max_delay (int) -> maximum delay in seconds

    Return:
    - returns a asyncio.Task. 
    """
    return asyncio.create_task(wait_random(max_delay))
