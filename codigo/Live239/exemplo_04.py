from parsel import Selector
from pathlib import Path

sel = Selector(text=Path('ddg_dunossauro.html').read_text())


links = sel.xpath('//a[@class="result__a"]')

for link in links:
    print(
        link.xpath('text()').get(),

        link.attrib['href']
    )
