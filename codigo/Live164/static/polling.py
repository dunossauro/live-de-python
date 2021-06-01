from browser import ajax, bind, document, html, timer


def on_complete(req):
    document['minha-div'] <= html.P(req.text)


def make_request():
    ajax.get('/dinamico/dado', oncomplete=on_complete)
    timer.set_timeout(make_request, 5000)


make_request()
