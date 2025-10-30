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



from timing_asgi import TimingMiddleware, TimingClient

class PrintTimings(TimingClient):
    def timing(self, metric_name, timing, tags):
        print(metric_name, timing, tags)

app = TimingMiddleware(app2, PrintTimings())


# from starlette.middleware.gzip import GZipMiddleware
# c_app = GZipMiddleware(app)


# from a2wsgi import ASGIMiddleware
# app_wsgi = ASGIMiddleware(c_app)


