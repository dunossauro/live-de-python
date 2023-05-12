from httpx import Client


with Client(
    base_url='https://httpbin.org', timeout=None,
    cookies={}
) as client:
    response = client.get('/delay/10')

print(response)
