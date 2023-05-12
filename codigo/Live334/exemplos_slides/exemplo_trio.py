import trio
import httpx

async def fetch_data():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://httpbin.org/get')
    return response.json()

async def main():
    async with trio.open_nursery() as nursery:
        response_data = await nursery.start_soon(fetch_data)
    print(response_data)

trio.run(main)
