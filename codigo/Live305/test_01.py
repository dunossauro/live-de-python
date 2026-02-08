import httpx
from httpx_retries import Retry, RetryTransport

retry = Retry(total=5, backoff_factor=0.5)

transport = RetryTransport(retry=retry)

with httpx.Client(transport=transport) as client:
    response = client.get(
        'https://dunossauro.co'
    )
