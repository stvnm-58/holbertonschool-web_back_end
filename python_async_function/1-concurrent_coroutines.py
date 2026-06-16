#!/usr/bin/env python3

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n : int, max_delay):
    delay = []
    tasks = []

    for _ in range(n):
        coroutine = wait_random(max_delay)
        nouvelle_tache = asyncio.create_task(coroutine)
        tasks.append(nouvelle_tache)
    
    for task in asyncio.as_completed(tasks):
        resultat = await task
        delay.append(resultat)
    
    return delay
