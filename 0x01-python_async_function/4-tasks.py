#!/usr/bin/env python3
"""defines an asynchronous coroutine task_wait_n"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times with the specified max_delay
    Args:
        n(int): number of times to spawn wait_random
        max_delay: maximum delay
    """
    delays = await asyncio.gather(*(task_wait_random(max_delay)
                                    for _ in range(n)))
    return sorted(delays)
