from bs4 import BeautifulSoup as bs
from requests import Session


url = 'http://torlinkbgs6aabns.onion/'

s = Session()
s.proxies = {'http': 'socks5h://127.0.0.1:9050'}

tor_links = s.get(url)
page = bs(tor_links.text, 'html.parser')
links = page.find('div', {'id': 'links'})

xpto = links.find_all(['h3', 'a'])
