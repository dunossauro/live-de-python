from babel import Locale
from babel.numbers import format_currency, format_decimal, parse_decimal
from decimal import Decimal

locale = Locale('pt', 'BR')
numero = Decimal('12345.67')

format_decimal(numero, locale=locale)  # 12.345,67
format_currency(numero, currency='BRL', locale=locale)
# R$ 12.345,67

parse_decimal('12.345,67', locale=locale)  # 12345.67
