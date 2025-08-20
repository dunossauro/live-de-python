from babel import Locale
from babel.dates import (
    LOCALTZ, format_date, format_datetime, format_time
)
from datetime import datetime

locale = Locale('pt', 'BR')
hora = datetime(2023, 8, 11, 15, 30, tzinfo=LOCALTZ)

format_date(hora, locale=locale)      # '11 de ago. de 2023'
format_time(hora, locale=locale)      # 15:30:00
format_datetime(hora, locale=locale)  # '11 de ago. de 2023 15:30:00'

format_date(hora, format='short', locale=locale) # 11/08/2023
format_date(hora, format='full', locale=locale)
# sexta-feira, 11 de agosto de 2023
