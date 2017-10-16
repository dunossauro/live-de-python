from db import engine, episodios
from download_samurai_x import lista_episodios

conn = engine.connect()

ins = episodios.insert()


def insert_db(t_values: tuple):
    return conn.execute(ins.values(temporada=t_values.temporada,
                                   episodio=t_values.episodio,
                                   nome=t_values.nome))


print(list(map(insert_db, lista_episodios)))
