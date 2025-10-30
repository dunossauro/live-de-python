from json import dumps
from typing import Callable
from wsgiref.simple_server import make_server

def get(path) -> tuple[bytes, str, str]:
    match path:
        case '/':
            return (
                dumps({'message': 'Olá!'}, ensure_ascii=False).encode('utf-8'),
                '200 OK',
                'application/json'
            )
        case '/html':
            return (
                b'<h1>PEI!</h1><p>um teste legal</p>',
                '200 OK',
                'text/html',
            )
        case _:
            return b'', '404 NOT FOUND', 'application/json'


def app(environ: dict, start_response: Callable):
    match environ['REQUEST_METHOD']:
        case 'GET':
            response_body, status, content_type = get(environ['PATH_INFO'])
        case _:
            response_body, status, content_type = b'', '404 NOT FOUND', ''

    response_headers = [('Content-type', content_type)]
    start_response(status, response_headers)

    return [response_body]


with make_server('', 8000, app) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()
