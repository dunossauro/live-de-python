from json import dumps
from typing import Callable


def get(path) -> tuple[bytes, str, str]:
    match path:
        case '/':
            return (
                dumps({'message': 'Olá!'}, ensure_ascii=False).encode('utf-8'),
                '200 OK',
                'application/json'
            )
        case '/html':
            return b'<h1>PEI!</h1><p>um teste legal</p>', '200 OK', 'text/html'
        case _:
            return b'', '404 NOT FOUND', 'application/json'


def app(environ: dict, start_response: Callable):
    """
    shell:

    gunicorn wsgi_app:app
    granian --interface wsgi wsgi_app:app
    """
    # pp(environ)

    match environ['REQUEST_METHOD']:
        case 'GET':
            response_body, status, content_type = get(environ['PATH_INFO'])
        case _:
            response_body, status, content_type = b'', '404 NOT FOUND', ''

    response_headers = [('Content-type', content_type)]
    start_response(status, response_headers)

    return [response_body]


async def app2(scope, receive, send):
    match scope['method']:
        case 'GET':
            response_body, status, content_type = get(scope['path'])
        case _:
            response_body, status, content_type = '', '404 NOT FOUND', ''

    response_headers = [(b'Content-type', content_type.encode('utf-8'))]
    await send({
            'type': 'http.response.start',
            'status': 200 if status == '200 OK' else 404,
            'headers': response_headers
        }
    )

    await send({
        'type': 'http.response.body',
        'body': response_body.encode('utf-8') if isinstance(response_body, str) else response_body
    })



environ = {
    'REQUEST_METHOD': 'GET',
    'QUERY_STRING': '',
    'RAW_URI': '/',
    'SERVER_PROTOCOL': 'HTTP/1.1',
    'HTTP_HOST': 'localhost:8000',
    'HTTP_USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64; rv:143.0) Gecko/20100101 '
    'Firefox/143.0',
    'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'HTTP_ACCEPT_LANGUAGE': 'en-US,en;q=0.5',
    'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br, zstd',
    'HTTP_SEC_GPC': '1',
    'HTTP_CONNECTION': 'keep-alive',
    'HTTP_UPGRADE_INSECURE_REQUESTS': '1',
    'HTTP_SEC_FETCH_DEST': 'document',
    'HTTP_SEC_FETCH_MODE': 'navigate',
    'HTTP_SEC_FETCH_SITE': 'none',
    'HTTP_SEC_FETCH_USER': '?1',
    'HTTP_DNT': '1',
    'HTTP_PRIORITY': 'u=0, i',
    'HTTP_PRAGMA': 'no-cache',
    'HTTP_CACHE_CONTROL': 'no-cache',
    'wsgi.url_scheme': 'http',
    'REMOTE_ADDR': '127.0.0.1',
    'REMOTE_PORT': '35938',
    'SERVER_NAME': '127.0.0.1',
    'SERVER_PORT': '8000',
    'PATH_INFO': '/',
    'SCRIPT_NAME': '',
}
