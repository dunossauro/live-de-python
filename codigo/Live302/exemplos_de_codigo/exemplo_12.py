class Contexto:

    def __init__(self, exc=ZeroDivisionError):
        self.exc = exc

    async def __aenter__(self):
        ...

    async def __aexit__(self, exc_type, exc_value, tb):
        if exc_type is self.exc:
            return True

async def main():
    async with Contexto(NameError):
        a + 1

import asyncio

asyncio.run(main())
