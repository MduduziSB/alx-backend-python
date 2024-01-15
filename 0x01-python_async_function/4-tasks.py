#!/usr/bin/env python3
"""
Takes the code from wait_n and alters it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random is being called.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """All tasks' delay"""
    delays: List[float] = []
    all_tasks: List[float] = []

    delays = [task_wait_random(max_delay) for _ in range(n)]

    all_tasks = [await delay for delay in asyncio.as_completed(delays)]

    return all_tasks
