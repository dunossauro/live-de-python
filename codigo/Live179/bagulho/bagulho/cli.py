from httpx import get


def cli():
    print(
        get(
            'http://httpbin.org/get?arg=Live de Python'
        ).json()['args']['arg']
    )
