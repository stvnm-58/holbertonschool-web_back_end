#!/usr/bin/env python3
"""Module pour exécuter plusieurs coroutines en parallèle et obtenir leurs résultats."""

import asyncio

# Importation dynamique de la fonction wait_random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Exécute wait_random n fois avec le max_delay spécifié.

    Les résultats sont renvoyés dans l'ordre où ils se terminent grâce
    à asyncio.as_completed.

    Args:
        n (int): Le nombre de fois que la coroutine doit être exécutée.
        max_delay (int): Le délai maximal pour chaque exécution.

    Returns:
        list[float]: Liste des délais générés, triés par ordre de complétion.
    """
    delays: list[float] = []
    tasks: list[asyncio.Task[float]] = []

    for _ in range(n):
        coroutine = wait_random(max_delay)
        nouvelle_tache = asyncio.create_task(coroutine)
        tasks.append(nouvelle_tache)

    for task in asyncio.as_completed(tasks):
        resultat = await task
        delays.append(resultat)

    return delays
