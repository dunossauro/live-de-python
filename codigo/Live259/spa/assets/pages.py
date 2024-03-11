from browser import ajax, bind, document, html, window


def post(url, data):
    def on_complete(request):
        ...

    ajax.post(
        f'http://{window.location.host}{url}',
        oncomplete=on_complete,
        blocking=True,
        data=data,
        headers={'Content-Type': 'application/json'},
    )


def get(url) -> list[dict[str, str]]:
    data = None

    def on_complete(request):
        nonlocal data
        data = request.json

    ajax.get(
        f'http://{window.location.host}{url}',
        oncomplete=on_complete,
        blocking=True,
    )

    return data


def index(root):
    response = get('/data')

    page = html.DIV('')
    h1 = html.H1('Minha Página SPA!')

    table = html.TABLE()
    tr_head = html.TR()
    for key in response[0].keys():
        tr_head <= html.TH(key)

    table <= tr_head

    for data in response:
        tr_data = html.TR()
        for value in data.values():
            tr_data <= html.TD(value)

        table <= tr_data

    button = html.BUTTON(
        'Ir para Cadastro',
        Class='btn btn-default',
        Type='submit',
        id='cadastro-btn',
    )

    page <= h1
    page <= table
    page <= button
    root <= page

    @bind(document['cadastro-btn'], 'click')
    def click_cadastro(event):
        router(page='cadastro')


def cadastro(root):
    root <= html.H1('Cadastro!')
    form = html.FORM(action='javascript:void(0)')
    form <= html.LABEL('Nome:')
    form <= html.BR()
    form <= html.INPUT(name='nome', Type='text', id='nome')
    form <= html.BR()
    form <= html.LABEL('Telefone:')
    form <= html.BR()
    form <= html.INPUT(name='telefone', Type='text', id='telefone')
    form <= html.BR()
    form <= html.BR()
    button = html.BUTTON('Enviar!', Class='btn btn-default', id='form-btn')

    form <= button
    root <= form

    @bind(document['form-btn'], 'click')
    def click_cadastro(event):
        data = window.JSON.stringify(
            {
                'nome': document['nome'].value,
                'telefone': document['telefone'].value,
            }
        )
        post('/cadastro', data)
        router(page='index')


def router(page):
    root = document['root']
    root.innerHTML = ''
    match page:
        case 'index':
            index(root)
        case 'cadastro':
            cadastro(root)


router(page='index')
