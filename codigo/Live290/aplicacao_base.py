"""
Exemplo da resposta da API
{
    'USDBRL': {
        'timestamp': '1618315045',
        'bid': '5.7276',
        'ask': '5.7282',
        'varbid': '-0.0054',
    },
    'BTCBRL': {...},
}
"""
import json
import urllib.request
from argparse import ArgumentParser
from datetime import datetime
from decimal import Decimal

# Definição do CLI para escolher as moedas
cli = ArgumentParser(description='BRL currency', epilog='Basic example of l10n')

cli.add_argument(
    '--currency',
    '-c',
    choices=['BTC', 'USD', 'EUR'],
    type=str,
    help='Reference currency for BRL comparison',
    required=True,
    action='append',
)

args = cli.parse_args()

# Requisição web para pegar os dados da cotação
currencies = ','.join(f'{c}-BRL' for c in args.currency)
url = f'https://economia.awesomeapi.com.br/json/last/{currencies}'

with urllib.request.urlopen(url) as response:
    response_data = response.read().decode('UTF-8')
    response_json = json.loads(response_data)


# Tratamento e apresentação dos dados de saída
cl = len(args.currency)

if cl > 1:
    print(
        f'Requested {cl} currencies for comparison against BRL: {args.currency}'
    )
else:
    print(f'Requested {args.currency[0]} currency for comparison against BRL')


for currency in sorted(args.currency):
    currency_data = response_json.get(f'{currency}BRL')
    trade_time = datetime.fromtimestamp(int(currency_data['timestamp']))

    if cl > 1:
        print(f'\n{currency}')

    print(f'Last trade: {trade_time}')
    print(f"Bid price: {Decimal(currency_data['bid']):n}")
    print(f"Ask price: {Decimal(currency_data['ask']):n}")
    print(f"Price variation: {Decimal(currency_data['varBid']):n}")
