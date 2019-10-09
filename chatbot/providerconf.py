"""Providers configuration.

See: https://bocadilloproject.github.io/guides/injection/
"""
from bocadillo import provider

# Define providers below.
@provider(scope="app")
async def diego():
    from .bot import diego

    return diego
