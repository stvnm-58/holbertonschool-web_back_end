#!/usr/bin/env python3
"""Module pour exécuter plusieurs tâches asyncio en parallèle via task_wait_random."""

import asyncio

# Importation dynamique de la fonction de la tâche 3
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """Exécute n tâches générées par task_wait_random en parallèle.

    Les résultats sont récupérés dans leur ordre de complétion.

    Args:
        n (int): Le nombre de tâches à créer.
        max_delay (int): Le délai maximal pour chaque tâche.

    Returns:
        list[float]: Liste des délais triés par ordre croissant de résolution.
    """
    delays: list[float] = []
    tasks: list[asyncio.Task[float]] = []

    for _ in range(n):
        nouvelle_tache = task_wait_random(max_delay)
        tasks.append(nouvelle_tache)

    for task in asyncio.as_completed(tasks):
        resultat = await task
        delays.append(resultat)

    return delays
