import time
import uuid
from http import HTTPStatus

import httpx
import hishel
import hishel.httpx
from httpx_retries import Retry, RetryTransport
from loguru import logger

proxy = httpx.Proxy("http://127.0.0.1:8080")
retry = Retry(total=2, backoff_factor=0.5)

proxy_transport = httpx.HTTPTransport(proxy=proxy, verify=False)

retry_transport = RetryTransport(proxy_transport, retry=retry)

transport = hishel.httpx.SyncCacheTransport(
    next_transport=retry_transport,
    storage=hishel.SyncSqliteStorage(),
)


def before_request(request: httpx.Request):
    request_id = str(uuid.uuid4())
    request.headers['X-Request-ID'] = request_id
    request.extensions['request_id'] = request_id
    request.extensions['start_time'] = time.monotonic()


def after_request(response: httpx.Response):
    request = response.request
    start = response.request.extensions.get("start_time", None)
    if start:
        elapsed = time.monotonic() - start
    else:
        elapsed = None

    logger.info(
        f'<sua DSL> {request.method} {request.url} {response.status_code} '
        f'{elapsed} {request.extensions.get("request_id")}'
    )


def get_page_content() -> str:
    with httpx.Client(
        transport=transport,
        event_hooks={'request': [before_request], 'response': [after_request]},
    ) as client:
        try:
            response = client.get('http://127.0.0.1:8000/delay/6')
            response.raise_for_status()
        except httpx.ReadTimeout:  # sua regra
            return ''
        except httpx.HTTPStatusError:  # sua regra
            return response.text
        else:
            return response.text

# ---





def test_get_page_content_timeout(respx_mock):
    mocked = respx_mock.get().mock(side_effect=httpx.ReadTimeout('timed out'))
    get_page_content()
    assert mocked.called


def test_get_page_content_server_error(respx_mock):
    mocked = respx_mock.get().mock(
        return_value=httpx.Response(
            HTTPStatus.INTERNAL_SERVER_ERROR, content=b'deu ruim no server :('
        )
    )
    content = get_page_content()
    assert mocked.called
    assert content == 'deu ruim no server :('


def test_get_page_content_timeout_retry(respx_mock):
    mocked = respx_mock.get().mock(
        side_effect=[
            httpx.ReadTimeout('pei'),
            httpx.Response(HTTPStatus.OK, content=b'Deu bom'),
        ]
    )

    content = get_page_content()

    assert mocked.call_count == 2
    assert content == 'Deu bom'


def test_get_page_content_etag(respx_mock):
    mocked = respx_mock.get()
    mocked.side_effect = [
        httpx.Response(
            HTTPStatus.OK, content=b'test', headers={'ETag': 'test-tag'}
        ),
        httpx.Response(HTTPStatus.NOT_MODIFIED),
    ]

    content_a = get_page_content()
    content_b = get_page_content()

    assert mocked.call_count == 2
    assert content_a == content_b
