#!/usr/bin/env python3
"""Module global pour la génération de nombres de manière asynchrone."""

import asyncio
import random


async def async_generator():
    """Génère dix nombres flottants aléatoires entre 0 et 10.

    Attend une seconde de manière asynchrone entre chaque génération.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
