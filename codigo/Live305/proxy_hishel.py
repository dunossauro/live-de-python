import httpx
import hishel
import hishel.httpx

proxy = httpx.Proxy('http://127.0.0.1:8080')

pure_transport = httpx.HTTPTransport(
    proxy=proxy, verify=False
)

transport = hishel.httpx.SyncCacheTransport(
    next_transport=pure_transport,
    storage=hishel.SyncSqliteStorage(),
)

with httpx.Client(transport=transport) as client:
    r1 = client.get('https://dunossauro.com')
    r2 = client.get('https://dunossauro.com')
    print(r1.status_code, r2.status_code)  # 200, 200
