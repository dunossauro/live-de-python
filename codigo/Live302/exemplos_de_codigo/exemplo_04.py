import asyncio


async def tarefa(n):
    await asyncio.sleep(n)
    print(f"Tarefa {n} concluída")


async def main():
    async with asyncio.timeout(1):
        await asyncio.gather(
            tarefa(0.5),
            tarefa(0.8),
            tarefa(10),
        )

asyncio.run(main())
