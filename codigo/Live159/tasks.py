from base64 import standard_b64encode

from celery import Celery
from celery.contrib import rdb
from httpx import post, get

app = Celery(
    broker='pyamqp://guest@localhost//'
)


@app.task
def ola_mundo():
    return 'olá mundo'


@app.task(
    name='Texto do documento',
    bind=True,
    retry_backoff=True,
    autoretry_for=(ValueError,)
)
def ocr_documento(self, documento):
    documento = open(documento, 'rb').read()

    image = standard_b64encode(documento).decode('utf-8')

    data = {
        'image': image
    }

    response = post(
        'http://live-159-external.herokuapp.com/document-to-text-choice',
        json=data,
        timeout=None
    )
    if response.status_code == 200:
        return response.json()

    raise ValueError('Deu erro')


class CPFError(BaseException):
    ...


@app.task(
    bind=True,
    autoretry_for=(CPFError,)
)
def validar_cpf_no_governo(self, cpf):
    if isinstance(cpf, dict):
        cpf = cpf['cpf']
    response = get(
        f'http://live-159-external.herokuapp.com/check-cpf?cpf={cpf}',
        timeout=None
    )
    # rdb.set_trace()
    if response.status_code == 200:
        return response.json()['cpf-status']
    raise CPFError('Erro no cpf!')
