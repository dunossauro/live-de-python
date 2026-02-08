from http import HTTPStatus

import httpx

def etag_maluca():
    url = 'https://dunossauro.com'

    resp = httpx.get(url)
    yield resp.text
    
    cached_etag = resp.headers.get('ETag')

    resp = httpx.get(url, headers={'If-None-Match': cached_etag})
    yield resp.text



def test_get_page_content_etag(respx_mock):
    mocked = respx_mock.get()
    mocked.side_effect = [
        httpx.Response(
            HTTPStatus.OK, content=b'test', headers={'ETag': 'test-tag'}
        ),
        httpx.Response(HTTPStatus.NOT_MODIFIED)
    ]

    em = etag_maluca()
    content_a = next(em)
    content_b = next(em)

    assert mocked.call_count == 2
    assert content_a == 'test'
    assert content_b == ''
