from functools import cache
from time import sleep
from medidor_de_tempo import medidor_de_tempo


@cache
@medidor_de_tempo
def delay(secs):
    """Bota o código para dormir por `secs`."""
    sleep(secs)
    return secs


print(delay(5), delay(5), delay(5))
