import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor as TPE
from concurrent.futures import ProcessPoolExecutor as PPE
from concurrent.futures import InterpreterPoolExecutor as IPE

MAX_WORKERS = 10
N_TASKS = 50

def task():
    n = 1
    for x in range(10_000_000):
        n += x + x * 2
    return n


def tpe():
    """ThreadPoolExecutor."""
    with TPE(max_workers=MAX_WORKERS) as pool:
        start = time.perf_counter()
        results = [pool.submit(task) for _ in range(N_TASKS)]

    print([x.result() for x in results][-1])
    print(f'Tempo passado (TPE): {time.perf_counter() - start}')


def ipe():
    """InterpreterPoolExecutor."""
    with IPE(max_workers=MAX_WORKERS) as pool:
        start = time.perf_counter()
        results = [pool.submit(task) for _ in range(N_TASKS)]

    print([x.result() for x in results][-1])
    print(f'Tempo passado (IPE): {time.perf_counter() - start}')


def ppe():
    """ProcessPoolExecutor."""
    with PPE(max_workers=MAX_WORKERS) as pool:
        start = time.perf_counter()
        results = [pool.submit(task) for _ in range(N_TASKS)]

    print([x.result() for x in results][-1])
    print(f'Tempo passado (PPE): {time.perf_counter() - start}')



if __name__ == '__main__':
    import sys
    print(f'GIL: {sys._is_gil_enabled()}')

    print(datetime.now())
    tpe()
    print(datetime.now())
    ipe()
    print(datetime.now())
    ppe()
    print(datetime.now())
