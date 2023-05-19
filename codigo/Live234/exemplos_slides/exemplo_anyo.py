import anyio
import httpx


async def fetch_data():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://httpbin.org/get')
    return response.json()


async def main():
    async with anyio.create_task_group() as tg:
        response_data = await tg.spawn(fetch_data)
    print(response_data)

anyio.run(main)
