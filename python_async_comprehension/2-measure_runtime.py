#!/usr/bin/env python3
"""Module pour mesurer le temps d'exécution de coroutines en parallèle."""

import asyncio
import time

# PEP 8 : Importation dynamique isolée des imports standards.
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """Mesure le temps d'exécution total de quatre coroutines.

    Exécute quatre instances de async_comprehension en parallèle et
    renvoie la durée totale en secondes.
    """
    start_time = time.time()

    # PEP 8 : asyncio.gather prend ici 4 arguments, l'alignement est propre.
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    return time.time() - start_time


async def main():
    """Affiche le temps d'exécution calculé."""
    runtime = await measure_runtime()
    print(f"Temps d'exécution total : {runtime:.2f} secondes")


if __name__ == "__main__":
    # Lance l'analyse de performance.
    asyncio.run(main())
