from browser import document, bind, ajax, window, timer, html
from random import randint

c_id = randint(10, 1_000)

def polling(event=None):
    status = document.select_one('div.status')
    poll = True

    def on_complete(request):
        nonlocal poll
        print('polling...')
        if request.status == 200:
            response = request.json['statuses']
            status.text = ''
            for st in response:
                status <= html.P(f"{st['status']}: {st['created_at']}")

                if st['status'] in ['envio', 'erro']:
                    poll = False

    ajax.get(
        f'http://{window.location.host}/status/{c_id}',
        oncomplete=on_complete,
        blocking=True,
    )

    if poll:
        timer.set_timeout(polling, 5_000)


@bind('#compra', 'click')
def faz_chamada(ev):
    def on_complete(request):
        if request.status == 201:
            document.select_one('#compra').disabled = True
            document.select_one('#msg') <= request.json['content']
            document.select_one('#msg') <= f'   --   id da compra # {c_id}'
            polling()

    data = window.JSON.stringify(
        {
            'c_id': window.encodeURIComponent(c_id),
            'p_id': window.encodeURIComponent(712631723),
        }
    )

    ajax.post(
        f'http://{window.location.host}/compra',
        headers={'Content-Type': 'application/json'},
        oncomplete=on_complete,
        data=data,
    )
