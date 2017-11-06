from requests import get
from bs4 import BeautifulSoup as bs
from calendar import monthrange

base_url = 'https://www.calendarr.com/brasil/calendario-outubro-2017/'
page = bs(get(base_url).text, 'lxml')

table = page.find('ul', {'class': 'list-holidays'})
days = table.find_all('li', {'class': 'list-holiday-box'})


def is_off(bs_day):
    """Diz se um dia é útil ou não."""
    if bs_day.find('div', {'class': 'list-holiday-dayweek holiday'}):
        return True
    return bs_day.text.strip().split()[1] in ['sáb', 'dom']


def get_day(bs_day):
    """Pega número do dia."""
    return bs_day.text.strip().split()[0]


offdays = set(map(int, map(get_day, filter(is_off, days))))
days = set(range(1, monthrange(2017, 11)[1] + 1)) - offdays
