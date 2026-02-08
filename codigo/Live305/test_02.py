import time
import uuid

import httpx
from loguru import logger

def before_request(request: httpx.Request):
    request_id = str(uuid.uuid4())
    request.headers['X-Request-ID'] = request_id
    request.extensions['request_id'] = request_id

def add_time(request: httpx.Request):
    request.extensions['start_time'] = time.monotonic() # isso é bom!

def after_request(response: httpx.Response):
    request = response.request
    start = response.request.extensions.get("start_time", None)
    if start:
        elapsed = time.monotonic() - start
    else:
        elapsed = None

    logger.info(
        f'{request.method} {request.url} {response.status_code} '
        f'{elapsed} {request.extensions.get("request_id")}'
    )
    
with httpx.Client(
    event_hooks={
        'request': [before_request, add_time],
        'response': [after_request]
    }
) as client:
    client.get('https://dunossauro.com')
