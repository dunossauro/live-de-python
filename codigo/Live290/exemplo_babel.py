import ctypes
import json
import locale
import urllib.request
from argparse import ArgumentParser
from datetime import datetime
from decimal import Decimal
from gettext import translation
from platform import system
from babel.dates import format_datetime
from babel.numbers import format_currency


if system() != 'Windows':
    localization, encode = locale.getlocale()
else:
    lcid = ctypes.windll.kernel32.GetUserDefaultLCID()
    localization = locale.windows_locale.get(lcid)
    encode = 'UTF-8'


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
    localization = args.language
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
    _('Last trade: {date}').format(
        date=format_datetime(trade_time, locale=localization)
    )
)

print(
    _('Bid price: {price}').format(
        price=format_currency(
            Decimal(parsed['bid']),
            currency='BRL',
            locale=localization
        )
    )
)

print(
    _('Ask price: {price}').format(
        price=format_currency(
            Decimal(parsed['ask']),
            locale=localization,
            currency='BRL',
        )
    )
)

print(
    _('Price variation: {variation}').format(
        variation=format_currency(
            Decimal(parsed['varBid']),
            locale=localization,
            currency='BRL',
        )
    )
)
