#!/usr/bin/env python3
"""Module fournissant un générateur de nombres aléatoires asynchrone."""

import asyncio
import random


async def async_generator():
    """Boucle 10 fois, attend 1 seconde à chaque tour et génère un nombre.

    Chaque nombre généré est un flottant aléatoire compris entre 0 et 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def main():
    """Consomme les valeurs du générateur asynchrone et les affiche."""
    async for number in async_generator():
        print(number)


if __name__ == "__main__":
    # Lance la boucle d'événements principale d'asyncio.
    asyncio.run(main())
