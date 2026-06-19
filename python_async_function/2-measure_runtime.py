#!/usr/bin/env python3
"""Module pour mesurer le temps d'exécution moyen de plusieurs coroutines."""

import asyncio
import time

# Importation dynamique de la fonction wait_n
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Mesure le temps d'exécution moyen par tâche pour wait_n.

    Args:
        n (int): Le nombre de tâches à exécuter.
        max_delay (int): Le délai maximal pour chaque tâche.

    Returns:
        float: Le temps total d'exécution divisé par n.
    """
    start_time: float = time.time()

    # Utilisation obligatoire de await à la place de asyncio.run()
    await wait_n(n, max_delay)

    total_time: float = time.time() - start_time

    return total_time / n
