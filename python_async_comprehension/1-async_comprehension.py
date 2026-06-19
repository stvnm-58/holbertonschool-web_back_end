#!/usr/bin/env python3
"""
This module provides a coroutine that uses an asynchronous comprehension
to collect and return a list of random floating-point numbers.
"""
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronously collects ten random numbers from the async generator
    using an asynchronous list comprehension and returns the gathered list.
    """
    return [i async for i in async_generator()]
