from download_samurai_x import lista_episodios

with open('episodios.csv', 'w') as _file:
    _file.write('Temporada; Episodio; Nome\n')
    for ep in lista_episodios:
        _file.write('{};{};{}\n'.format(ep.temporada, ep.episodio, ep.nome))
