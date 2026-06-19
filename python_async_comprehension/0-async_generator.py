#!/usr/bin/env python3
"""
This module provides an asynchronous generator coroutine that loops
ten times, waiting one second per iteration, and yields random floats.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously loops ten times, pausing for one second per iteration,
    and then yields a random floating-point number between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
