from pprint import pp


def app(environ: dict, start_response: callable):
    environ_data = {
        var: environ[var]
        for var in environ
        if var.startswith('HTTP') or var.startswith('wsgi')
    }
    pp(environ_data)
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [b"Hello world!\n"]


from wsgiref.simple_server import make_server
with make_server('', 8000, app) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()
