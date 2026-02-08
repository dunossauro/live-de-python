import httpx
url = 'https://dunossauro.com'

# 1a request
resp = httpx.get(url)
print(f'status: {resp.status_code}')  # 200: OK
print(resp.elapsed)

cached_etag = resp.headers.get('ETag')

# 2a request
resp = httpx.get(url, headers={'If-None-Match': cached_etag})
print(f'status: {resp.status_code}')  # 304: Not Modified
print(resp.elapsed)
