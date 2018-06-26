from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
from requests import get
from functools import partial
from os import getpid

l_urls = ['https://google.com'] * 6

# executor = ThreadPoolExecutor(max_workers=3)
# result = executor.map(get, l_urls)
# print(result)


print('Threads')
with ThreadPoolExecutor(max_workers=3) as executor:
    """
    executor.__enter__ -> self (ThreadPoolExecutor)
    executor.__exit__ -> executor.shutdown(wait=True)
    """
    result = executor.map(get, l_urls)
    print(result)

print(list(result))

print('Processo')
with ProcessPoolExecutor() as executor:
    result = executor.map(partial(print, getpid()))
    print(result)

print(list(result))
