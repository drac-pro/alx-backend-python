#!/usr/bin/env python3
"""defines an asynchronous coroutine wait_random"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """asynchronous coroutine that waits for a random delay between
    0 and max_delay  seconds and eventually returns it.
    Args:
        max_delay(int): maximum delay
    Return:
        float: time the function waited for
    """
    t = random.uniform(0, max_delay)
    await asyncio.sleep(t)
    return t
