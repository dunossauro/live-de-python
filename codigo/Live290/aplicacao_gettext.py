import urllib.request
from argparse import ArgumentParser
from datetime import datetime
from decimal import Decimal
from gettext import translation
import json

t = translation('messages', localedir='locale', fallback=True)
t.install()
_ = t.gettext
ngettext = t.ngettext

# Definição do CLI para escolher as moedas
cli = ArgumentParser(
    description=_('BRL currency'), epilog=_('Basic example of l10n')
)

cli.add_argument(
    '--currency',
    '-c',
    choices=['BTC', 'USD', 'EUR'],
    type=str,
    help=_('Reference currency for BRL comparison'),
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
print(
    ngettext(
        'Requested %(currencies)s currency for comparison against BRL',
	    'Requested %(cl)s currencies for comparison against BRL: %(currencies)s',
        cl,
    ) % {'cl': cl, 'currencies': args.currency}
)


for currency in sorted(args.currency):
    currency_data = response_json.get(f'{currency}BRL')
    trade_time = datetime.fromtimestamp(int(currency_data['timestamp']))

    if cl > 1:
        print(f'\n{currency}')

    print(_('Last trade: {trade_time}').format(trade_time=trade_time))
    print(_('Bid price: {price}').format(price=Decimal(currency_data['bid'])))
    print(_('Ask price: {price}').format(price=Decimal(currency_data['ask'])))
    print(_('Price variation: {price}').format(
        price=Decimal(currency_data['varBid'])
    ))
