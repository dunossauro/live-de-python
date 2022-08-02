from time import sleep
from medidor_de_tempo import medidor_de_tempo


@medidor_de_tempo
def delay(secs):
    """Bota o código para dormir por `secs`."""
    sleep(secs)
    return secs


@medidor_de_tempo
def soma(x, y):
    return x +y
