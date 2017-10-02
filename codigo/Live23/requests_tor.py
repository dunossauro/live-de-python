from requests import Session, get

# com tor
s = Session()
s.proxies = {'http': 'socks5://127.0.0.1:9050'}

xpto = s.get('http://httpbin.org/ip')
print(xpto.json())


# sem tor
g = get('http://httpbin.org/ip')
print(g.json())
