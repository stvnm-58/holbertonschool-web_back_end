#!/usr/bin/env python3

import asyncio

# On importe la fonction du fichier 3
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int):
    delay = []
    tasks = []
    
    for _ in range(n):
    
        nouvelle_tache = task_wait_random(max_delay)
        tasks.append(nouvelle_tache)
    
    for task in asyncio.as_completed(tasks):
        resultat = await task
        delay.append(resultat)
    
    return delay
