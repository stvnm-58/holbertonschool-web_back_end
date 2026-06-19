#!/usr/bin/env python3
"""Module fournissant un générateur de nombres aléatoires asynchrone."""

import asyncio
from collections.abc import AsyncGenerator
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """Génère dix nombres flottants aléatoires entre 0 et 10.

    Attend une seconde de manière asynchrone entre chaque génération.

    Yields:
        float: Un nombre aléatoire compris entre 0 et 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
