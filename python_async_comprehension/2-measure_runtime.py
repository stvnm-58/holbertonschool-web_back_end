#!/usr/bin/env python3
"""
This module provides a coroutine that measures the total runtime
of executing an asynchronous comprehension coroutine four times in parallel.
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total execution time of running async_comprehension
    four times concurrently using asyncio.gather, then returns the duration.
    """
    start_time = time.time()

    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)

    end_time = time.time()
    return end_time - start_time
