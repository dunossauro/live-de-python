from browser import ajax, bind, document, html


def on_complete(req):
    document['minha-div'] <= html.P(req.text)


@bind('#btn', 'click')
def click_btn(evt):
    ajax.get('/dinamico/dado', oncomplete=on_complete)
