#!/usr/bin/env python3
"""Module pour collecter des données asynchrones via une compréhension."""

import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """Collecte les 10 nombres du générateur asynchrone.

    Renvoie une liste contenant l'ensemble des flottants générés.
    """
    return [i async for i in async_generator()]


async def main():
    """Affiche la liste finale une fois collectée."""
    result = await async_comprehension()
    print(result)


if __name__ == "__main__":
    # Lance l'exécution globale.
    asyncio.run(main())
