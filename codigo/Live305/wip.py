from http import HTTPStatus

import httpx
from respx import MockRouter
from httpx_retries import Retry, RetryTransport

retry = Retry(
    total=1,
    backoff_factor=0.5,
    status_forcelist=[418]
)
transport = RetryTransport(retry=retry)


def get_page_content() -> str:
    with httpx.Client(
        transport=transport,
        timeout=3,
        base_url='http://127.0.0.1:8000'
    ) as client:  # Próximo tópico!
        try:
            response = client.get(
                '/delay/6',
            )
            response.raise_for_status()
        except httpx.ReadTimeout: # sua regra
            return ''
        except httpx.HTTPStatusError: # sua regra
            return ''
        else:
            return response.text


def test_get_page_content_timeout(respx_mock: MockRouter):
    mocked = respx_mock.get().mock(
        side_effect=httpx.ReadTimeout('timed out')
    )
    content = get_page_content()
    assert mocked.called
    assert content == ''


def test_get_page_content_server_error(respx_mock: MockRouter):
    mocked = respx_mock.get().mock(
        return_value=httpx.Response(
            HTTPStatus.INTERNAL_SERVER_ERROR,
            content=b'deu ruim no server :('
        ))
    content = get_page_content()

    assert mocked.called
    assert content == ''


def test_get_page_content_timeout_retry(respx_mock: MockRouter):
    mocked = respx_mock.get().mock(
        side_effect=[
            httpx.ReadTimeout('pei'),
            httpx.Response(HTTPStatus.OK, content=b'Deu bom')
        ]
    )

    content = get_page_content()

    assert mocked.call_count == 2
    assert content == 'Deu bom'
