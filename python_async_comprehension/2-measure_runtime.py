#!/usr/bin/env python3
import asyncio
import time

# Importation dynamique de la tâche 1
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime():
    start_time = time.time()
    
    # On lance les 4 exécutions en parallèle
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    
    end_time = time.time()
    return end_time - start_time
