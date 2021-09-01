from sqlalchemy import (create_engine, MetaData, Column,
                        Table, Integer, String, ForeignKey, select)


engine = create_engine('sqlite:///base.db',
                       echo=False)

metadata = MetaData(bind=engine)

artists = Table('artistas', metadata,
                Column('id', Integer, primary_key=True, autoincrement=True),
                Column('nome', String(40), index=True,
                       nullable=False, unique=True))

discs = Table('discos', metadata,
              Column('id', Integer, primary_key=True, autoincrement=True),
              Column('artista_id', ForeignKey('artistas.id'), nullable=False),
              Column('album', String(40), nullable=False),
              Column('ano', Integer, nullable=False))

metadata.create_all()


def search_albums(artist):
    artist_id = [x for x in select([artists.c.id]).
                 where(artists.c.nome == artist.lower()).execute()]

    if artist_id:
        query = select([discs.c.id, discs.c.album,
                        discs.c.ano, discs.c.artista_id]).where(
                        discs.c.artista_id == artist_id[0][0]).execute()

        return {_id: {'album': album,
                      'ano': ano,
                      'id_artista': artista}
                for _id, album, ano, artista in query}

    return {}


def id_artist(artist):
    searched = select([artists]).where(artists.c.nome == artist)
    result = [_id for _id, artist in searched.execute()]
    if result:
        return result[0]

    else:
        insert_artist(artist)
        return id_artist(artist)

def search_all_artists():
    return {_id: artist for _id, artist in select([artists]).execute()}


def insert_artist(artist):
    conn = engine.connect()

    artista_ins = artists.insert()

    new_artist = artista_ins.values(nome=artist)

    try:
        conn.execute(new_artist)
        status = True
    except Exception as e:
        print(e)
        status = False
    finally:
        conn.close()
        return status


def insert_album(disc, year, artist):
    conn = engine.connect()

    disc_ins = discs.insert()
    new_disc = disc_ins.values(artista_id=id_artist(artist),
                               album=disc,
                               ano=year)

    try:
        conn.execute(new_disc)
        status = True
    except Exception as e:
        print(e)
        status = False
    finally:
        conn.close()
        return status
