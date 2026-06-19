#!/usr/bin/env python3
"""
This module provides an asynchronous function to execute multiple
coroutines concurrently and return their results in ascending order.
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.
    Returns the list of all the delays in ascending order.
    """
    delays: List[float] = []
    taches = [wait_random(max_delay) for _ in range(n)]

    for tache_terminee in asyncio.as_completed(taches):
        delay = await tache_terminee
        delays.append(delay)

    return delays
