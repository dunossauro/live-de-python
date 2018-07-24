from aiofiles import open as aopen
from asyncio import get_event_loop

async def write_file():
    async with aopen('teste.txt', 'w') as f:
        await f.write('bananas')


loop = get_event_loop()
loop.run_until_complete(write_file())
