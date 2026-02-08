import httpx
import hishel
import hishel.httpx
from httpx_retries import Retry, RetryTransport

proxy = httpx.Proxy("http://127.0.0.1:8080")
retry = Retry(total=5, backoff_factor=0.5)

proxy_transport = httpx.HTTPTransport(
    proxy=proxy, verify=False
)

retry_transport = RetryTransport(proxy_transport, retry=retry)

transport = hishel.httpx.SyncCacheTransport(
    next_transport=retry_transport,
    storage=hishel.SyncSqliteStorage(),
)

with httpx.Client(transport=transport) as client:
    r1 = client.get('https://httpbin.org/status/502')
    print(r1.status_code)
