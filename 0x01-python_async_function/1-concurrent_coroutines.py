#!/usr/bin/env python3
"""defines an asynchronous coroutine wait_n"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """spawn wait_random n times with the specified max_delay
    Args:
        n(int): number of times to spawn wait_random
        max_delay: maximum delay
    """
    routines = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    result = await asyncio.gather(*routines)
    return sorted(result)
