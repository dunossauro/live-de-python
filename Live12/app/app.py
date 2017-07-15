"""
Loja de Cds.

Live 12: <>
"""
from json import dumps
from bottle import Bottle, request, response
from app.core import search_all_artists, insert_artist, insert_album, search_albums

app = Bottle()


@app.get('/')
def index_map():
    """Retornar um mapa completo da API."""
    return dumps({"artistas": "url/artistas",
                  "albuns": "url/albuns"})


@app.get('/artistas')
def artistas_map():
    """
    Retorna todos os artistas.
    """
    return search_all_artists()


@app.post('/artista')
def post_artist():
    """
    Isere dados na API.

    Formato do input:
    Content-Type: application/json
    {"nome": "Zimbra"}
    """
    artista = request.json
    response.headers['Content-Type'] = 'application/json'

    if not artista:
        response.status = 400
        return {response.status: artista}

    if insert_artist(artista['nome'].lower()):
        response.status = 201  # Created
    else:
        response.status = 409  # Conflict

    return dumps({response.status: artista})


@app.post('/album')
def post_albums():
    """
    {
     "nome": "Vem",
     "artista":"Mallu",
     "ano": 2017
    }
    """
    disc = request.json
    response.headers['Content-Type'] = 'application/json'

    if not disc:
        response.status = 400
        return {response.status: disc}

    if insert_album(disc['nome'], disc['ano'], disc['artista'].lower()):
        response.status = 201  # Created
    else:
        response.status = 409  # Conflict

    return dumps({response.status: disc})



@app.get('/albums/<artist>')
def albums_map(artist):
    return search_albums(artist)


if __name__ == '__main__':
    app.run()
