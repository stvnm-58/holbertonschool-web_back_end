#!/usr/bin/env python3
"""
This module provides a function task_wait_n that uses task_wait_random
to execute multiple concurrent tasks and return their results.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay.
    Returns the list of all the delays in ascending order.
    """
    delays: List[float] = []
    taches = [task_wait_random(max_delay) for _ in range(n)]

    for tache_terminee in asyncio.as_completed(taches):
        delay = await tache_terminee
        delays.append(delay)

    return delays
