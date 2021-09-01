"""Exemplo de DOC."""
from requests import get


def endpoint_up(endpoint_url) -> tuple:
    if not endpoint_url.startswith('http'):
        endpoint_url = f'http://{endpoint_url}'

    request = get(endpoint_url)
    status_code = request.status_code

    # se retornar OK
    if status_code in [200, 201, 202, 302, 304]:
        return True, request.status_code

    # se der erro no endpoint
    elif request.status_code in range(500, 506):
        return False, 'bad request'

    # qualquer coisa não prevista
    else:
        return False, 'Deu ruim'
