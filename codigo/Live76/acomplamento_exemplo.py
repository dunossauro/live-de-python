"""Exemplo simples de complamento."""
from requests import get


def page_content(url: str, ssl: bool = False, *, params=None) -> str:
    prefix = 'https' if ssl else 'http'
    return get(f'{prefix}://{url}', params).content.decode()
