#!/usr/bin/env python3
"""Module de test pour vérifier le bon fonctionnement de async_generator."""

import asyncio

# Importation dynamique de ton fichier (remplace '0-async_generator' par le
# nom réel de ton fichier si nécessaire, sans l'extension .py).
async_generator = __import__('0-async_generator').async_generator


async def main() -> None:
    """Consomme les valeurs générées par async_generator et les affiche."""
    print("Début de la récupération des valeurs...")

    async for value in async_generator():
        print(f"Valeur reçue : {value}")

    print("Fin de la génération.")


if __name__ == "__main__":
    asyncio.run(main())