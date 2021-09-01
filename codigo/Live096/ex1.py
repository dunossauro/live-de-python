import requests
import time


# httpbin.org - testar clientes/requisições HTTP
def get(url, **kwargs):
    t0 = time.time()
    response = requests.get(url, **kwargs)
    print(response.status_code, time.time() - t0)
    return response


if __name__ == "__main__":
    get("https://httpbin.org/status/302")
