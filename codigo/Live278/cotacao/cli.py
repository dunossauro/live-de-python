from typing import Literal
from cyclopts import App
import httpx
from rich import print

app = App()

BASE_URL = 'https://economia.awesomeapi.com.br/json/last/{}'

@app.default
def cotacao(
    moeda: Literal['USD', 'BRL', 'BTC'] = 'USD'
):
    response = httpx.get(
        BASE_URL.format(moeda), timeout=None
    )
    print(response.json())


app()
