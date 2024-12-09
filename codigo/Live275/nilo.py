import time
import threading
import multiprocessing
import contextlib

CARGA = 10_000_000

import sys, sysconfig

if sys.version_info.minor != 12:
    versions = {
        'Tier 2': 'TIER2' in sysconfig.get_config_var("PY_CORE_CFLAGS"),
        'JIT': 'Py_JIT' in sysconfig.get_config_var("PY_CORE_CFLAGS"),
        'GIL': sys._is_gil_enabled()
    }

    print(versions)


def trabalho(name):
    # print(f" + Trabalho {name} iniciando")
    z = 0
    for i in range(CARGA):
        z += i
    # print(f" - Trabalho {name} acabando")


@contextlib.contextmanager
def cronometro(mensagem):
    start_time = time.time()
    yield
    end_time = time.time()
    print(f"{mensagem}: Tempo: {end_time - start_time}")


def com_threads():
    threads = []
    for i in range(multiprocessing.cpu_count()):
        threads.append(threading.Thread(target=trabalho, args=(i,)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


def sem_threads():
    for z in range(multiprocessing.cpu_count()):
        trabalho(z)


if __name__ == "__main__":
    with cronometro("Com threads"):
        com_threads()
    with cronometro("Sem threads"):
        sem_threads()
