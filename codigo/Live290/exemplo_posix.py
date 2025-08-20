import json
import locale
import urllib.request
from argparse import ArgumentParser
from datetime import datetime
from decimal import Decimal
from gettext import translation

localization, encode = locale.getlocale()

locale.setlocale(locale.LC_ALL, f'{localization}.{encode}')

t = translation('messages', localedir='locale', fallback=True)
t.install(f'{localization}.{encode}')
_ = t.gettext

cli = ArgumentParser(_('Basic example of l10n'))

cli.add_argument(
    '--currency',
    '-c',
    choices=['BTC', 'USD', 'EUR'],
    type=str,
    help=_('Reference currency for BRL comparison'),
    required=True,
)


# === Adição
cli.add_argument(
    '--language',
    '-l',
    choices=['pt_BR', 'en_US', 'eo'],
    default=localization,
    help=_('Preferred languange for the answer'),
)

args = cli.parse_args()

if args.language != localization:
    # TODO: Abstrair essa lógica em outro lugar
    locale.setlocale(locale.LC_ALL, f'{args.language}.{encode}')
    t = translation(
        'messages',
        localedir='locale',
        languages=[args.language],
        fallback=True,
    )
    t.install()
    _ = t.gettext


url = f'https://economia.awesomeapi.com.br/json/last/{args.currency}-BRL'

with urllib.request.urlopen(url) as response:
    response_data = response.read().decode('UTF-8')
    parsed = json.loads(response_data).get(f'{args.currency}BRL')

trade_time = datetime.fromtimestamp(int(parsed['timestamp']))

print(
    _('Last trade: {trade_time}').format(
        trade_time=datetime.strftime(
            trade_time, locale.nl_langinfo(locale.D_T_FMT)
        )
    )
)

print(
    _('Bid price: {price}').format(
        price=locale.currency(Decimal(parsed['bid']), grouping=True)
    )
)

print(
    _('Ask price: {price}').format(
        price=locale.currency(Decimal(parsed['ask']), grouping=True)
    )
)

print(
    _('Price variation: {variation}').format(
        variation=locale.currency(Decimal(parsed['varBid']), grouping=True)
    )
)
