import ezodf

doc = ezodf.opendoc('episodios.ods')
# type(doc)
folhas = list(doc.sheets.names())
ep_folha = doc.sheets[folhas[0]]
linhas = sum(list(ep_folha.rows()), [])

print(list(map(lambda x: x.value, linhas)))
