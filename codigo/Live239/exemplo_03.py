from parsel import Selector
from httpx import get

response = get(
    'https://dunossauro.com/', follow_redirects=True
)


sel = Selector(text=response.content.decode())

print(
    sel
    .xpath('//*[@class="button"]/text()')
    .getall()
)
