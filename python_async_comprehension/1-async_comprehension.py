#!/usr/bin/env python3
"""Module pour collecter des données asynchrones dans une liste typée."""

import asyncio

# Importation dynamique du générateur asynchrone
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list[float]:
    """Collecte 10 nombres flottants du générateur asynchrone.

    Returns:
        list[float]: Une liste contenant les 10 nombres générés.
    """
    return [i async for i in async_generator()]
