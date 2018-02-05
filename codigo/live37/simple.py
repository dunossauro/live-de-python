from configparser import ConfigParser
from requests import get

d = {'verbose': 0,
     'url': 'http://google.com',
     'port': 8080,
     'bananas': 'pijamas'}

e = {'verbose': 0,
     'url': 'http://google.com',
     'port': 8080,
     'bananas': 'pijamas'}

config = ConfigParser(d,
                      allow_no_value=True,
                      delimiters=('=', ':', '-'),
                      comment_prefixes=('#', ';'),
                      inline_comment_prefixes='#',
                      strict=False,
                      )

config['DEFAULT'] = e
config.read('example.ini')
default_config = dict(config['default'])
xpto_config = dict(config['xpto'])
xpto2_config = dict(config['xpto2'])

print(default_config)
print(xpto_config)
print(xpto2_config)
print(default_config['url'],
      get(default_config['url']))
