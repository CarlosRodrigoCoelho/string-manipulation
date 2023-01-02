# https://www.bytebank.com.br/exchange

import re

url = 'www.bytebank.com.br/exchange'
pattern_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/exchange')
match = pattern_url.match(url)

if not match:
    raise ValueError('Invalid URL.')
print('Valid URL!')
