#!/usr/bin/env python3
"""Module pour créer et planifier une tâche asyncio à partir d'une coroutine."""

import asyncio

# Importation dynamique de la fonction wait_random
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task[float]:
    """Crée et renvoie une tâche asyncio qui exécute wait_random.

    Args:
        max_delay (int): Le délai maximal pour la coroutine.

    Returns:
        asyncio.Task[float]: La tâche asynchrone planifiée.
    """
    coro = wait_random(max_delay)
    return asyncio.create_task(coro)
