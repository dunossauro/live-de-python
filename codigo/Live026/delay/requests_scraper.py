import requests


for delay in [1, 2, 3, 4, 5]:
    url = "http://httpbin.org/delay/{}".format(delay)
    requests.get(url)
    print(url)
