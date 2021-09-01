"""https://osf.io/w8u26/."""
import asyncio
import time

def primo(n: int) -> bool:
    return not any(n//i == n/i
                   for i in range(n-1, 1, -1))

async def maior_primo_menor_que(n: int) -> None:
    print(f'Maior primo até {n}')
    for val in range(n-1, 0, -1):
        if primo(val):
            print(f'Maior primo: {val}')
            return val
        await asyncio.sleep(0.01)

async def main():
    t0 = time.time()
    await asyncio.wait([
        maior_primo_menor_que(2),
        maior_primo_menor_que(10000),
        maior_primo_menor_que(1000),
        maior_primo_menor_que(100)
    ])
    t1 = time.time()
    print('Levou %.2f ms' % (1000*(t1-t0)))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
