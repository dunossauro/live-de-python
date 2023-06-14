from parsel import Selector
from dataclasses import dataclass


@dataclass
class Live:
    título: str | None
    link: str


final = []

sel = Selector(text=open('todas_as_lives.html').read())

lives = sel.css('a#video-title-link')

lives = sel.xpath('//a[@id="video-title-link"]')

for live in lives:
    final.append(
        Live(
            live.css('yt-formatted-string::text').get(),
            f'http://youtube.com{live.attrib["href"]}'
        )
    )

print(final[0])
